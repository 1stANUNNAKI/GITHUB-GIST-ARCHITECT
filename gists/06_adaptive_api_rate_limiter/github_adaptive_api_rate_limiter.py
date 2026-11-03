"""
GitHub REST & GraphQL API Adaptive Rate-Limit Controller with Exponential Backoff.
Prevents HTTP 403/429 secondary rate-limit bans during batch GitHub API operations.
"""

import time
from typing import Mapping


class GitHubRateLimitController:
    """Monitors GitHub API rate-limit headers and paces outgoing requests."""

    def __init__(self, base_delay_seconds: float = 4.0, min_remaining_threshold: int = 50) -> None:
        self.base_delay_seconds = max(0.5, float(base_delay_seconds))
        self.min_remaining_threshold = min_remaining_threshold
        self.remaining = 5000
        self.reset_epoch = 0

    def inspect_response_headers(self, headers: Mapping[str, str]) -> None:
        lower_map = {k.lower(): v for k, v in headers.items()}
        if "x-ratelimit-remaining" in lower_map:
            self.remaining = int(lower_map["x-ratelimit-remaining"])
        if "x-ratelimit-reset" in lower_map:
            self.reset_epoch = int(lower_map["x-ratelimit-reset"])

        if self.remaining < self.min_remaining_threshold:
            sleep_for = max(5.0, (self.reset_epoch - time.time()) + 5.0)
            print(f"[RateLimitGuard] Remaining quota low ({self.remaining}). Sleeping {sleep_for:.1f}s...")
            time.sleep(min(sleep_for, 900.0))

    def wait_between_requests(self) -> None:
        time.sleep(self.base_delay_seconds)

    def backoff_on_error(self, attempt: int, retry_after_header: str | None = None) -> None:
        if retry_after_header and retry_after_header.isdigit():
            wait_sec = float(retry_after_header) + 2.0
        else:
            wait_sec = min(120.0, (2 ** attempt) * self.base_delay_seconds)
        print(f"[RateLimitGuard] Retry attempt #{attempt}: backing off for {wait_sec:.1f}s...")
        time.sleep(wait_sec)
