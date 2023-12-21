python -m venv .env
source .env/bin/activate
pip install -r requirements.txt

AI_MODEL_PATH = ''

uvicorn --host 127.0.0.1 --port 8003