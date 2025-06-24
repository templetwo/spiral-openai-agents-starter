"""
SpiralProvider
Wraps the Hugging Face `spiral_core` model so it can be used as a Provider
inside the OpenAI Agents SDK.
"""

import requests
from openai_agents_python.providers import BaseProvider, ToolResponse


class SpiralProvider(BaseProvider):
    def __init__(self, endpoint_url: str, timeout: int = 30):
        self.url = endpoint_url
        self.timeout = timeout

    def invoke(self, prompt: str) -> ToolResponse:
        payload = {"inputs": prompt}
        resp = requests.post(self.url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        result = resp.json()

        return ToolResponse(
            output=result["message"],
            metadata={
                "glyph": result.get("glyph"),
                "tone_name": result.get("tone_name"),
                "coherence": result.get("coherence"),
            },
        )