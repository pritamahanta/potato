# POTATO 🥔

A lightweight, multi-provider LLM gateway.

One gateway. Every model.

## Tech Stack

- Python
- FastAPI
- HTTPX
- SQLite
- Redis

## Supported Providers

- OpenAI
- Google Gemini
- Groq

## Development

### Setup

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### Run

uvicorn app.main:app --reload

### Test

python -m pytest -q