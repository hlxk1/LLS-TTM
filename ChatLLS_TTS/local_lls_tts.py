# llm & tts
# 使用本地模型用 
import os
import ChatTTS
from IPython.display import Audio
import torch
import torchaudio


base_path = r'F:\AI_LLM\ChatTTS-0601\ChatTTS'
chat = ChatTTS.Chat()
chat.load_models(source='local',local_path=base_path)

# # LLM
# from openai import OpenAI

# client = OpenAI(api_key="lm-studio", base_url="http://localhost:10086/v1")
# que = input("请提问")
# response = client.chat.completions.create(
#     model="Qwen/Qwen1.5-14B-Chat-GGUF",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": que},
#     ],
#     stream=False
# )
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:10086/v1", api_key="lm-studio")
que = input("请提问")
completion = client.chat.completions.create(
  model="Qwen/Qwen1.5-14B-Chat-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": que}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
# TTS
# texts = [str(response.choices[0].message.content),]
texts = [str(completion.choices[0].message.content),]
print(texts)
wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)
# 输出语音保存
output_path = os.path.join(os.getcwd(), "output.wav")
try:
    torchaudio.save(output_path, torch.from_numpy(wavs[0]).unsqueeze(0), 24000)
except:
    torchaudio.save(output_path, torch.from_numpy(wavs[0]), 24000,format='wav')

import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # 降低语速
engine.say("你好，这是一段语音输出。")
engine.runAndWait()