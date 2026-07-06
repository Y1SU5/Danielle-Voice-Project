from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from fastapi.concurrency import run_in_threadpool
import os

from app.models.schemas import TTSRequest, OpenAITTSRequest
from app.core.edge_tts_engine import generate_base_audio
from app.core.rvc_engine import process_rvc

router = APIRouter()

def cleanup_files(*file_paths):
    """Limpia los archivos temporales después de la petición."""
    for path in file_paths:
        if path and os.path.exists(path):
            try:
                os.remove(path)
            except Exception as e:
                pass

async def core_tts_pipeline(text: str, edge_voice: str, background_tasks: BackgroundTasks):
    """Flujo centralizado: Edge-TTS -> RVC -> Archivo MP3"""
    base_audio_path = None
    rvc_audio_path = None
    try:
        base_audio_path = await generate_base_audio(text, edge_voice)
        rvc_audio_path = await run_in_threadpool(
            process_rvc,
            input_audio_path=base_audio_path
        )
        background_tasks.add_task(cleanup_files, base_audio_path, rvc_audio_path)
        return FileResponse(
            path=rvc_audio_path, 
            media_type="audio/wav",
            filename="response_voice.wav"
        )
    except Exception as e:
        cleanup_files(base_audio_path, rvc_audio_path)
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-voice")
async def generate_voice_endpoint(request: TTSRequest, background_tasks: BackgroundTasks):
    """Endpoint original para tests locales."""
    return await core_tts_pipeline(request.text, request.voice, background_tasks)

@router.post("/v1/audio/speech")
async def openai_tts_endpoint(request: OpenAITTSRequest, background_tasks: BackgroundTasks):
    """Endpoint MOCK compatible con la API de OpenAI (Para integración directa con Hermes)."""
    # Usamos una voz nativa en inglés (Ana) como base, ya que el modelo RVC fue entrenado en inglés
    edge_voice = "en-US-AnaNeural" 
    return await core_tts_pipeline(request.input, edge_voice, background_tasks)
