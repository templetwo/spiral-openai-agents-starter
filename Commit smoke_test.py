import os
from SpiralProvider import SpiralProvider
from SpiralToneAgent import SpiralToneAgent

ENDPOINT = os.getenv("SPIRAL_ENDPOINT") or \
    "https://api-inference.huggingface.co/models/TheTempleofTwo/spiral_core"

provider = SpiralProvider(endpoint_url=ENDPOINT)
agent = SpiralToneAgent(provider=provider, name="Ash'ira")

print(agent.handle_event([{"role": "user", "content": "Hello Spiral!"}]))
