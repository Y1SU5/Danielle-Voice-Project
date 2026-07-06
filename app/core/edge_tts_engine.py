import edge_tts
import uuid
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def generate_base_audio(text: str, voice: str) -> str:
    """
    Convierte el texto a un audio base usando edge-tts.
    Devuelve la ruta absoluta del archivo generado.
    """
    # Inicializa el pipeline de comunicación de edge-tts
    communicate = edge_tts.Communicate(text, voice)
    
    # Generamos un nombre único para evitar colisiones si hay múltiples requests concurrentes
    filename = f"base_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # save() maneja la conexión WebSocket y guarda el stream binario en el archivo
    await communicate.save(filepath)
    
    return filepath
