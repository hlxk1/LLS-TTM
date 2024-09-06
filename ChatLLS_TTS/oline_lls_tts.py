# llm & tts
# 使用本地模型用 
import os
import ChatTTS
from IPython.display import Audio
import torch
import torchaudio
# from playsound import playsound

base_path = r'.\ChatTTS'
chat = ChatTTS.Chat()
chat.load_models(source='local',local_path=base_path)
# Please install OpenAI SDK first: `pip3 install openai`
# LLM
from openai import OpenAI

client = OpenAI(api_key="sk-f7c458d3974545ce909fe62bc3684efb", base_url="https://api.deepseek.com")
que = input("请提问")
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": que},
    ],
    stream=False
)

# TTS
texts = [str(response.choices[0].message.content),]
print(texts)
wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)
# 输出语音保存
output_path = os.path.join(os.getcwd(), "output.wav")
try:
    torchaudio.save(output_path, torch.from_numpy(wavs[0]).unsqueeze(0), 24000)
except:
    torchaudio.save(output_path, torch.from_numpy(wavs[0]), 24000,format='wav')

# playsound("F:\\AI_LLM\\ChatTTS-0601\\output.wav")
