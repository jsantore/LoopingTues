import sounddevice as sd

from kokoro_onnx import Kokoro

kokoro = Kokoro("kokoro-v1.0.onnx",
                "voices-v1.0.bin")
samples, sample_rate = kokoro.create(
    "Hello. Comp 151! We are speaking now", voice="af_sarah", speed=1.0, lang="en-us"
)
print("Playing audio...")
sd.play(samples, sample_rate)
sd.wait()