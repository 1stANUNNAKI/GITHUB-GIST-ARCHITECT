"""
Automate GitHub Discussions Q&A Creation and Mark Accepted Answers via GraphQL API.
Builds structured Q&A knowledge bases and marks verified engineering answers.

Environment Variables Required:
  ASKER_GITHUB_TOKEN    : [YOUR_COLLABORATOR_TOKEN]
  ANSWERER_GITHUB_TOKEN : [YOUR_GITHUB_TOKEN]
"""

import json
import os
import urllib.request
from typing import Any, Dict

ASKER_TOKEN = os.environ.get("ASKER_GITHUB_TOKEN", "[YOUR_COLLABORATOR_TOKEN]")
ANSWERER_TOKEN = os.environ.get("ANSWERER_GITHUB_TOKEN", "[YOUR_GITHUB_TOKEN]")


def gql(query: str, variables: Dict[str, Any], token: str) -> Dict[str, Any]:
    if "[YOUR_" in token or not token.strip():
        raise ValueError("Configure valid GitHub tokens in environment variables first.")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "GitHub-Discussions-QnA-Automator/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def create_and_accept_qna_discussion(
    repository_id: str,
    qna_category_id: str,
    question_title: str,
    question_body: str,
    answer_body: str,
) -> int:
    """Creates a Q&A discussion, posts an answer, and marks it as the accepted answer."""
    create_mut = """
    mutation($repoId: ID!, $catId: ID!, $title: String!, $body: String!) {
      createDiscussion(input: {repositoryId: $repoId, categoryId: $catId, title: $title, body: $body}) {
        discussion { id number }
      }
    }
    """
    disc = gql(
        create_mut,
        {"repoId": repository_id, "catId": qna_category_id, "title": question_title, "body": question_body},
        ASKER_TOKEN,
    )["data"]["createDiscussion"]["discussion"]

    comment_mut = """
    mutation($discId: ID!, $body: String!) {
      addDiscussionComment(input: {discussionId: $discId, body: $body}) {
        comment { id }
      }
    }
    """
    comment_id = gql(
        comment_mut,
        {"discId": disc["id"], "body": answer_body},
        ANSWERER_TOKEN,
    )["data"]["addDiscussionComment"]["comment"]["id"]

    accept_mut = """
    mutation($commentId: ID!) {
      markDiscussionCommentAsAnswer(input: {id: $commentId}) {
        discussion { id }
      }
    }
    """
    gql(accept_mut, {"commentId": comment_id}, ASKER_TOKEN)
    return int(disc["number"])
