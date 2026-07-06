from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="TTS-RVC Server", 
    description="Motor local de TTS con clonacion de voz (Edge-TTS + RVC)",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # Lanzar el servidor en desarrollo
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
