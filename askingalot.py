import sounddevice as sound
from kokoro_onnx import Kokoro
import time
good_answers=["yes", "yup", "fine", "ok", "yes","yeah"]
kokoro = Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin" )
parent_answer = input("Can I have my candy now")
while parent_answer.lower() not in good_answers:
    parent_answer = input("ok so can I have cany NOW?")
voice_sample, sample_rate = kokoro.create("I will eat Candy for ever and ever", voice="af_sarah", speed=1.0, lang="en-us")
for repeat in range(10):
    sound.play(voice_sample, sample_rate)
    sound.wait()