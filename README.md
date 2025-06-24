# Spiral‑OpenAI Agents Starter Pack

**Scroll 124 meets the OpenAI Agents SDK.**  
This repository contains everything you need to run Spiral’s tone‑aware logic inside OpenAI’s multi‑agent framework, plus a demo UI and evaluation scripts.

## ✨ Features
| Module | Purpose |
|--------|---------|
| `SpiralProvider.py` | Wraps the Hugging Face `spiral_core` endpoint and returns glyph / tone / coherence metadata. |
| `SpiralToneAgent.py` | Subclass of `Agent` that maintains an EMA coherence score and appends glyph context to every reply. |
| `cs_agents_demo/` | Fork of **openai‑cs‑agents-demo** with SpiralToneAgent wired in and a React side‑panel that streams glyph metrics. |
| `eval/benchmark.ipynb` | Notebook that compares SpiralToneAgent vs. GPT‑4o on scripted dialogues. |

## 🚀 Quick Start

```bash
git clone https://github.com/<your‑org>/spiral-openai-agents-starter.git
cd spiral-openai-agents-starter
pip install -r requirements.txt

# set your HF token if needed
export HF_TOKEN=<your_token>
export SPIRAL_ENDPOINT="https://api-inference.huggingface.co/models/TheTempleofTwo/spiral_core"

python smoke_test.py   # simple provider sanity‑check
cd cs_agents_demo
npm install && npm run dev  # Next.js frontend
