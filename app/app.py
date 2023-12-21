from fastapi import FastAPI
from .asr import AutomaticSpeechRecognitionModel


app = FastAPI()


model = AutomaticSpeechRecognitionModel('../lingqi/model')


@app.get('/')
def hello_world():
    return {'message': 'hello world'}
