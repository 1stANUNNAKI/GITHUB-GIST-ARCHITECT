<#
.SYNOPSIS
    Publishes all 10 sanitized Gist bundles and the 3 Master Collection Index Gists
    to https://gist.github.com/1stANUNNAKI after verifying OAuth 'gist' scope.
#>
$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Owner = $env:GITHUB_USERNAME
if (-not $Owner) { $Owner = "1stANUNNAKI" }

function Get-StoredToken([string]$User) {
    $env:GCM_INTERACTIVE = "never"
    $env:GIT_TERMINAL_PROMPT = "0"
    $p = New-Object System.Diagnostics.Process
    $p.StartInfo.FileName = "git"
    $p.StartInfo.Arguments = "credential fill"
    $p.StartInfo.UseShellExecute = $false
    $p.StartInfo.RedirectStandardInput = $true
    $p.StartInfo.RedirectStandardOutput = $true
    $p.Start() | Out-Null
    $p.StandardInput.Write("protocol=https`nhost=github.com`nusername=$User`n`n")
    $p.StandardInput.Close()
    $p.WaitForExit(5000) | Out-Null
    $out = $p.StandardOutput.ReadToEnd()
    if ($out -match "password=(.+)") { return $Matches[1].Trim() }
    return $null
}

$Token = $env:GITHUB_TOKEN
if (-not $Token -or $Token -match "YOUR_") {
    $Token = Get-StoredToken $Owner
}

$NeedGistScope = $true
if ($Token) {
    try {
        $check = Invoke-WebRequest -Method "GET" -Uri "https://api.github.com/user" -Headers @{
            "Authorization" = "Bearer $Token"
            "User-Agent"    = "GitHubGistArchitect"
        } -UseBasicParsing
        $scopes = "$($check.Headers['X-OAuth-Scopes'])"
        if ($scopes -match "\bgist\b") {
            $NeedGistScope = $false
        } else {
            Write-Host "[INFO] Current token scopes ($scopes) do not include 'gist'. Requesting 'gist' scope upgrade..."
        }
    } catch {}
}

if ($NeedGistScope) {
    $ClientId = "01ab8ac9400c4e429b23"
    $devResp = Invoke-RestMethod -Method "POST" -Uri "https://github.com/login/device/code" `
        -Headers @{ "Accept" = "application/json"; "User-Agent" = "Git-Credential-Manager" } `
        -Body @{ client_id = $ClientId; scope = "repo workflow gist" }
    try { Set-Clipboard -Value $devResp.user_code } catch {}
    try { Start-Process $devResp.verification_uri } catch {}
    Write-Host "=========================================================="
    Write-Host "AUTHORIZE GIST SCOPE FOR $Owner"
    Write-Host "1. Open URL : $($devResp.verification_uri)"
    Write-Host "2. Enter Code: $($devResp.user_code) (Copied to clipboard!)"
    Write-Host "=========================================================="
    $pollInterval = [Math]::Max([int]$devResp.interval, 5) + 1
    $deadline = (Get-Date).AddSeconds([int]$devResp.expires_in)
    while ((Get-Date) -lt $deadline) {
        Start-Sleep -Seconds $pollInterval
        $tokResp = Invoke-RestMethod -Method "POST" -Uri "https://github.com/login/oauth/access_token" `
            -Headers @{ "Accept" = "application/json"; "User-Agent" = "Git-Credential-Manager" } `
            -Body @{
                client_id   = $ClientId
                device_code = $devResp.device_code
                grant_type  = "urn:ietf:params:oauth:grant-type:device_code"
            }
        if ($tokResp.access_token) {
            $Token = $tokResp.access_token
            $approveStr = "protocol=https`nhost=github.com`nusername=$Owner`npassword=$Token`n`n"
            $p = New-Object System.Diagnostics.Process
            $p.StartInfo.FileName = "git"
            $p.StartInfo.Arguments = "credential approve"
            $p.StartInfo.UseShellExecute = $false
            $p.StartInfo.RedirectStandardInput = $true
            $p.Start() | Out-Null
            $p.StandardInput.Write($approveStr)
            $p.StandardInput.Close()
            $p.WaitForExit(5000) | Out-Null
            Write-Host "Token upgraded with 'gist' scope!"
            break
        }
    }
}

$Headers = @{
    "Authorization" = "Bearer $Token"
    "Accept"        = "application/vnd.github+json"
    "User-Agent"    = "GitHubGistArchitect/1.0"
}

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Manifest = Get-Content -Raw -Path "$RepoRoot\gists\gist_catalog_manifest.json" -Encoding UTF8 | ConvertFrom-Json
$Published = @()

foreach ($item in $Manifest) {
    $folder = "$RepoRoot\gists\$($item.folder)"
    $codeContent = [System.IO.File]::ReadAllText("$folder\$($item.filename)", [System.Text.Encoding]::UTF8)
    $guideContent = [System.IO.File]::ReadAllText("$folder\$($item.guide_filename)", [System.Text.Encoding]::UTF8)

    $body = @{
        description = $item.seo_title
        public      = $true
        files       = @{
            $item.guide_filename = @{ content = $guideContent }
            $item.filename       = @{ content = $codeContent }
        }
    } | ConvertTo-Json -Depth 6

    $res = Invoke-RestMethod -Method "POST" -Uri "https://api.github.com/gists" -Headers $Headers -ContentType "application/json; charset=utf-8" -Body ([System.Text.Encoding]::UTF8.GetBytes($body))
    Write-Host "[PUBLISHED GIST #$($item.id)] $($res.html_url) -> $($item.seo_title)"
    $Published += [PSCustomObject]@{
        id         = $item.id
        collection = $item.collection
        title      = $item.seo_title
        filename   = $item.filename
        url        = $res.html_url
    }
    Start-Sleep -Seconds 2
}

# Publish Master Catalog List Gist
$ indexLines = @(
    "# 📚 Master GitHub Automation & Profile Engineering Gist Catalog",
    "",
    "| # | Collection | Gist Title | Direct Link | File |",
    "| :-: | :--- | :--- | :---: | :--- |"
)
foreach ($p in $Published) {
    $indexLines += "| #$($p.id) | $($p.collection) | **$($p.title)** | [Open Gist]($($p.url)) | ``$($p.filename)`` |"
}
$masterBody = @{
    description = "[Master Gist List] Curated GitHub Profile Telemetry, GraphQL GPG PR Automation & Security Suite"
    public      = $true
    files       = @{
        "00_MASTER_GIST_LIST.md" = @{ content = ($indexLines -join "`n") }
    }
} | ConvertTo-Json -Depth 6
$masterRes = Invoke-RestMethod -Method "POST" -Uri "https://api.github.com/gists" -Headers $Headers -ContentType "application/json; charset=utf-8" -Body ([System.Text.Encoding]::UTF8.GetBytes($masterBody))
Write-Host "`n[MASTER LIST GIST PUBLISHED] $($masterRes.html_url)"
