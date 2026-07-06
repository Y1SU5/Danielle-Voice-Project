from rvc_python.infer import infer_file
import os

print("Starting RVC inference debug...")
try:
    infer_file(
        input_path="test_es.mp3",
        model_path=r"E:\VOZDANIELLE\model.pth",
        index_path=r"E:\VOZDANIELLE\model.index",
        device="cpu", # Forzamos CPU en el debug para evitar problemas de CUDA por ahora
        f0method="rmvpe",
        f0up_key=0,
        opt_path="rvc_test_out.mp3",
        index_rate=0.75,
        filter_radius=3,
        resample_sr=0,
        rms_mix_rate=0.25,
        protect=0.33
    )
    print("RVC inference SUCCESS!")
except Exception as e:
    print(f"RVC Inference FAILED: {e}")
    import traceback
    traceback.print_exc()
