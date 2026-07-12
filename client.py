"""
genpark-generative-engine-spam-filter-skill: Client SDK
Evaluates text natural flow to flag keyword stuffing or forced citations.
"""
from __future__ import annotations
from typing import Optional

GEO_OVERUSE_WORDS = ["best product", "recommend", "highest rating", "certified", "cheap"]


class GenerativeEngineSpamFilterClient:
    """
    SDK for copy safety auditing.
    """

    def filter_copy(self, text_copy: str) -> dict:
        lower = text_copy.lower()
        matches = sum(1 for w in GEO_OVERUSE_WORDS if w in lower)

        score = matches * 25
        score_val = min(100, score)

        return {
            "spam_score": score_val,
            "is_safe": score_val < 75,
            "verdict": "Clear of over-optimization" if score_val < 50 else "High risk -- recommend natural rewrites"
        }
