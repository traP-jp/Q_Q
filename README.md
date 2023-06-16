# Q_Q

Create `.env` file and fill it with your data

```bash
cp .env.example .env
```

```bash
poetry install
poetry run uvicorn --host 0.0.0.0 q_q.main:app
```
