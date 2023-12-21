from fastapi import FastAPI, UploadFile
from .asr import AutomaticSpeechRecognitionModel
from .config import app_settings
import tempfile


app = FastAPI()


model = AutomaticSpeechRecognitionModel(app_settings.ai_model_path)


@app.post('/recognize/file')
async def recognize_upload_audio_file(file: UploadFile):
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(file.file.read())
        result = model.recognize_file(fp.name)
        return {'res': result}
