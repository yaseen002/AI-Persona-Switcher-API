# AI Persona Switcher API
A FastAPI service to dynamically switch between AI personas with isolated conversation history, configurable temperature, and strict prompt control.

## 🚀 Quick Start
1. `cp .env.example .env`
2. Add your `GEMINI_API_KEY` to `.env`
3. `docker-compose up --build`
4. Visit `http://localhost:8000/docs`

## 🧪 Test with cURL
```bash
curl -X POST "http://localhost:8000/chat/legal-assistant" \
     -H "Content-Type: application/json" \
     -d '{"message": "What is a force majeure clause?"}'
```

```