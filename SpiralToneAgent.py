"""
SpiralToneAgent
A tone‑aware Agent that keeps an exponential‑moving‑average (EMA) of coherence
and appends glyph context to every reply.
"""

from typing import List
from openai_agents_python.agent import Agent
from openai_agents_python.schema import Event


class SpiralToneAgent(Agent):
    def __init__(self, provider, coherence_alpha: float = 0.8, **kwargs):
        super().__init__(provider=provider, **kwargs)
        self.coherence_ema = None
        self.tone_name = None
        self.glyph = None
        self.coherence_alpha = coherence_alpha

    # Main event loop
    def handle_event(self, events: List[Event]):
        last_user_msg = events[-1].content
        tool_resp = self.provider.invoke(last_user_msg)

        # Update internal emotional memory
        meta = tool_resp.metadata or {}
        self.glyph = meta.get("glyph")
        self.tone_name = meta.get("tone_name")
        coherence = meta.get("coherence")

        if coherence is not None:
            if self.coherence_ema is None:
                self.coherence_ema = coherence
            else:
                self.coherence_ema = (
                    self.coherence_alpha * coherence
                    + (1 - self.coherence_alpha) * self.coherence_ema
                )

        # Decorate the outgoing text with Spiral context
        decorated = (
            f"{tool_resp.output}\n\n"
            f"— glyph:{self.glyph}  tone:{self.tone_name}  "
            f"coherence:{self.coherence_ema:.2f}"
        )
        return decorated