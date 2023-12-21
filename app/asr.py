import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


class AutomaticSpeechRecognitionModel:

    def __init__(self, model_path: str) -> None:
        device = "cpu"
        torch_dtype = torch.float32
        self._model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_path, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        self._model.to(device)
        self._processor = AutoProcessor.from_pretrained(model_path)
        self._pipe = pipeline(
            "automatic-speech-recognition",
            model=self._model,
            tokenizer=self._processor.tokenizer,
            feature_extractor=self._processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=30,
            batch_size=16,
            torch_dtype=torch_dtype,
            device=device,
        )

    def recognize_file(self, path: str) -> str:
        result = self._pipe(path, enerate_kwargs={"language": "mandarin"})
        return result["text"]
