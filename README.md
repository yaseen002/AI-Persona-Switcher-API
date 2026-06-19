# 🤖 AI Persona Switcher API

A production-style FastAPI backend that allows users to dynamically switch between different AI personas. Each persona has distinct behavior, tone, and knowledge restrictions, demonstrating professional LLM API integration, prompt engineering, and session-based state management.

## 🌟 Features
- **Multi-Persona Support**: Strict Legal Assistant, Medical Advisor, Code Reviewer, and Custom personas.
- **Stateful Conversations**: In-memory session management allows for multi-turn context-aware chats.
- **Strict Data Validation**: Pydantic models ensure all incoming and outgoing data is strictly typed and validated.
- **Secure Configuration**: Environment variables (`.env`) used for all API keys and sensitive configurations.
- **Production-Ready Architecture**: Separation of concerns (Routes, Services, Models, Session Management).

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python 3.11+)
- **LLM Provider**: Mistral AI API (via HTTPX Async Client)
- **Data Validation**: Pydantic v2
- **Containerization**: Docker & Docker Compose

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (for local development)
- Docker & Docker Compose (for containerized deployment)
- A free Mistral AI API key (or OpenAI/Gemini)

### 1. Clone and Setup
```bash
git clone https://github.com/yaseen002/AI-Persona-Switcher-API
cd ai-persona-switcher