"""
Create GPG-Verified Commits & Merge Pull Requests via GitHub GraphQL API.
Uses the official `createCommitOnBranch` GraphQL mutation so every commit is
cryptographically signed by GitHub (`signature.isValid = true` / "Verified").

Environment Variables Required:
  GITHUB_TOKEN : [YOUR_GITHUB_TOKEN]
"""

import base64
import json
import os
import urllib.request
from typing import Dict, Any

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "[YOUR_GITHUB_TOKEN]")


def graphql_request(query: str, variables: Dict[str, Any], token: str = GITHUB_TOKEN) -> Dict[str, Any]:
    if "[YOUR_" in token or not token.strip():
        raise ValueError("Set a valid GITHUB_TOKEN in your environment before running.")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "GraphQL-GPG-PR-Automator/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def create_gpg_verified_pr(
    owner: str,
    repo: str,
    branch_name: str,
    file_path: str,
    file_content: str,
    headline: str,
    coauthor_trailer: str = "Co-authored-by: [COAUTHOR_NAME] <[COAUTHOR_ID]+[COAUTHOR_LOGIN]@users.noreply.github.com>",
) -> int:
    """Creates a GPG-signed commit on a branch, opens a PR, and merges it via GraphQL."""
    info_query = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        id
        defaultBranchRef {
          name
          target { oid }
        }
      }
    }
    """
    info = graphql_request(info_query, {"owner": owner, "name": repo})["data"]["repository"]
    repo_id = info["id"]
    base_branch = info["defaultBranchRef"]["name"]
    head_oid = info["defaultBranchRef"]["target"]["oid"]

    # Create branch ref via REST
    ref_req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}/git/refs",
        data=json.dumps({"ref": f"refs/heads/{branch_name}", "sha": head_oid}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(ref_req, timeout=15).close()
    except Exception:
        pass

    commit_mutation = """
    mutation($input: CreateCommitOnBranchInput!) {
      createCommitOnBranch(input: $input) {
        commit { oid signature { isValid } }
      }
    }
    """
    encoded = base64.b64encode(file_content.encode("utf-8")).decode("ascii")
    commit_vars = {
        "input": {
            "branch": {"repositoryNameWithOwner": f"{owner}/{repo}", "branchName": branch_name},
            "message": {"headline": headline, "body": coauthor_trailer},
            "fileChanges": {"additions": [{"path": file_path, "contents": encoded}]},
            "expectedHeadOid": head_oid,
        }
    }
    c_res = graphql_request(commit_mutation, commit_vars)
    is_valid = c_res["data"]["createCommitOnBranch"]["commit"]["signature"]["isValid"]
    print(f"Created GPG-Signed Commit (Verified={is_valid})")

    pr_mutation = """
    mutation($input: CreatePullRequestInput!) {
      createPullRequest(input: $input) {
        pullRequest { id number }
      }
    }
    """
    pr_res = graphql_request(
        pr_mutation,
        {
            "input": {
                "repositoryId": repo_id,
                "baseRefName": base_branch,
                "headRefName": branch_name,
                "title": headline,
                "body": headline,
            }
        },
    )
    pr_node = pr_res["data"]["createPullRequest"]["pullRequest"]

    merge_mutation = """
    mutation($input: MergePullRequestInput!) {
      mergePullRequest(input: $input) {
        pullRequest { merged number }
      }
    }
    """
    graphql_request(merge_mutation, {"input": {"pullRequestId": pr_node["id"], "mergeMethod": "MERGE"}})
    return int(pr_node["number"])
