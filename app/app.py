from fastapi import FastAPI, UploadFile
from .asr import AutomaticSpeechRecognitionModel
import tempfile


app = FastAPI()


model = AutomaticSpeechRecognitionModel('../lingqi/model')


@app.post('/recognize/file')
async def recognize_upload_audio_file(file: UploadFile):
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(file.file.read())
        result = model.recognize_file(fp.name)
        return {'res': result}
