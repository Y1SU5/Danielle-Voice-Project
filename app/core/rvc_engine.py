import os
import shutil
import torch

# MONKEY PATCH: PyTorch 2.6+ cambió torch.load a weights_only=True por defecto.
# RVC y Fairseq necesitan cargar objetos completos, así que forzamos weights_only=False.
_original_torch_load = torch.load
def _patched_torch_load(*args, **kwargs):
    kwargs['weights_only'] = False
    return _original_torch_load(*args, **kwargs)
torch.load = _patched_torch_load

try:
    from rvc_python.infer import RVCInference
    RVC_AVAILABLE = True
except ImportError:
    RVC_AVAILABLE = False
    print("Advertencia: rvc_python no está instalado.")

VOICE_DIR = r"E:\VOZDANIELLE"
MODEL_PATH = os.path.join(VOICE_DIR, "model.pth")
INDEX_PATH = os.path.join(VOICE_DIR, "model.index")

# Variable global para mantener el modelo cargado en memoria RAM/VRAM
rvc_model_instance = None

def get_rvc_instance():
    global rvc_model_instance
    if not RVC_AVAILABLE:
        return None
        
    if rvc_model_instance is None:
        print(f"Cargando modelo RVC en memoria desde {MODEL_PATH}...")
        try:
            # Inicializamos el modelo solo la primera vez para no perder tiempo en cada request
            rvc_model_instance = RVCInference(
                device="cuda:0", # Cambiar a cpu si no tienes tarjeta NVIDIA
                model_path=MODEL_PATH,
                index_path=INDEX_PATH,
                version="v2"
            )
            # Configuramos los parámetros óptimos para la clonación
            rvc_model_instance.set_params(
                f0method="rmvpe",
                f0up_key=8,  # +12 semitonos para subir el tono y darle un timbre más femenino y natural
                index_rate=0.75,
                filter_radius=3,
                resample_sr=0,
                rms_mix_rate=0.25,
                protect=0.33
            )
            print("Modelo RVC cargado exitosamente.")
        except Exception as e:
            print(f"Error al cargar el modelo RVC: {e}")
            rvc_model_instance = None
            
    return rvc_model_instance

def process_rvc(input_audio_path: str, model_name: str = None, index_name: str = None) -> str:
    """
    Toma un audio base, lo pasa por el modelo RVC de Danielle y devuelve la ruta del audio convertido.
    """
    output_path = input_audio_path.replace("base_", "rvc_").replace(".mp3", ".wav")
    
    rvc = get_rvc_instance()
    
    if rvc is None:
        print("ADVERTENCIA: RVC no disponible. Devolviendo voz original...")
        shutil.copy2(input_audio_path, output_path)
        return output_path
        
    try:
        print(f"Clonando voz... ({input_audio_path} -> {output_path})")
        # Inferencia con la instancia global ya cargada en memoria
        rvc.infer_file(input_audio_path, output_path)
        print("Clonación completada.")
    except Exception as e:
        print(f"Error procesando RVC durante la inferencia: {e}")
        import traceback
        traceback.print_exc()
        shutil.copy2(input_audio_path, output_path)
        
    return output_path
