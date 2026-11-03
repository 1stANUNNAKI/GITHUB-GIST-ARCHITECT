"""
Generate Custom GitHub Streak & Stats SVG Card Locally (Midnight Galaxy Palette).
Eliminates third-party SVG server caching and downtime by rendering crisp vector
cards directly inside your repository via Python.
"""

from dataclasses import dataclass


@dataclass
class StreakMetrics:
    total_contributions: int
    joined_range: str
    current_streak: int
    current_range: str
    longest_streak: int
    longest_range: str


MIDNIGHT_GALAXY_PALETTE = {
    "bg": "#060B1E",
    "border": "#5B5C8A",
    "title": "#8087E2",
    "ring": "#8087E2",
    "fire": "#FACC15",
    "text": "#DEE7F0",
    "muted": "#9098BF",
}


def render_streak_svg(metrics: StreakMetrics, palette: dict = MIDNIGHT_GALAXY_PALETTE) -> str:
    """Renders a unified Midnight Galaxy streak-stats.svg vector card."""
    total_fmt = f"{metrics.total_contributions:,}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="495" height="195" viewBox="0 0 495 195" fill="none">
  <rect x="1" y="1" width="493" height="193" rx="6" fill="{palette['bg']}" stroke="{palette['border']}" stroke-width="2"/>
  <line x1="165" y1="28" x2="165" y2="167" stroke="{palette['border']}" stroke-opacity="0.5"/>
  <line x1="330" y1="28" x2="330" y2="167" stroke="{palette['border']}" stroke-opacity="0.5"/>

  <!-- Total Contributions -->
  <g transform="translate(82.5, 0)" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif">
    <text x="0" y="78" fill="{palette['text']}" font-size="28" font-weight="700">{total_fmt}</text>
    <text x="0" y="114" fill="{palette['title']}" font-size="14" font-weight="600">Total Contributions</text>
    <text x="0" y="142" fill="{palette['muted']}" font-size="12">{metrics.joined_range}</text>
  </g>

  <!-- Current Streak -->
  <g transform="translate(247.5, 0)" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif">
    <circle cx="0" cy="70" r="36" stroke="{palette['ring']}" stroke-width="4.5" fill="none"/>
    <text x="0" y="30" fill="{palette['fire']}" font-size="18">🔥</text>
    <text x="0" y="80" fill="{palette['fire']}" font-size="26" font-weight="800">{metrics.current_streak}</text>
    <text x="0" y="130" fill="{palette['title']}" font-size="14" font-weight="700">Current Streak</text>
    <text x="0" y="152" fill="{palette['muted']}" font-size="12">{metrics.current_range}</text>
  </g>

  <!-- Longest Streak -->
  <g transform="translate(412.5, 0)" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif">
    <text x="0" y="78" fill="{palette['text']}" font-size="28" font-weight="700">{metrics.longest_streak}</text>
    <text x="0" y="114" fill="{palette['title']}" font-size="14" font-weight="600">Longest Streak</text>
    <text x="0" y="142" fill="{palette['muted']}" font-size="12">{metrics.longest_range}</text>
  </g>
</svg>
"""


if __name__ == "__main__":
    sample = StreakMetrics(
        total_contributions=4200,
        joined_range="2020 - Present",
        current_streak=5,
        current_range="Active Streak",
        longest_streak=14,
        longest_range="Best Record",
    )
    with open("streak-stats.svg", "w", encoding="utf-8") as out:
        out.write(render_streak_svg(sample))
    print("Generated streak-stats.svg successfully.")
