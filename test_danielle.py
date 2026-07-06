import requests
import json
import os

url = "http://localhost:8000/generate-voice"

payload = json.dumps({
  "text": "Hello Yisus! My name is Danielle. If you can hear this audio, it means our artificial intelligence server and voice cloning are working perfectly. You are a genius!",
  "voice": "en-US-AriaNeural",
  "rvc_model": "model.pth",
  "rvc_index": "model.index"
})

headers = {
  'Content-Type': 'application/json'
}

print("Enviando texto a Danielle (Servidor Local en puerto 8000)...")
print("Por favor, espera unos segundos mientras la tarjeta gráfica clona la voz...")

try:
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        audio_file = "prueba_danielle.mp3"
        with open(audio_file, "wb") as f:
            f.write(response.content)
        print(f"¡ÉXITO ABSOLUTO! 🎉 Audio guardado como '{audio_file}'.")
        
        # Reproducir el audio automáticamente en Windows
        try:
            os.startfile(audio_file)
        except Exception:
            pass
    else:
        print(f"Error del servidor: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("ERROR: No se pudo conectar al servidor. Asegúrate de que 'uvicorn app.main:app' esté corriendo.")
