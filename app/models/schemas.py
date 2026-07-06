from pydantic import BaseModel
from typing import Optional

class TTSRequest(BaseModel):
    text: str
    voice: str = "es-ES-ElviraNeural"  # Voz femenina base recomendada para Danielle
    rvc_model: str = "model.pth" 
    rvc_index: str = "model.index" 

# Agregamos el formato de OpenAI para hacerlo compatible con Hermes de forma nativa
class OpenAITTSRequest(BaseModel):
    model: str = "tts-1"
    input: str
    voice: str = "danielle"
    response_format: str = "mp3"
    speed: float = 1.0
