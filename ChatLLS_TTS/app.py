import os
import gradio as gr
import ChatTTS
import torch
import torchaudio
from openai import OpenAI
from IPython.display import Audio

base_path = r'.\ChatTTS'
chat = ChatTTS.Chat()
chat.load_models(source='local', local_path=base_path)

# Initialize OpenAI client
client = OpenAI(api_key="sk-f7c458d3974545ce909fe62bc3684efb", base_url="https://api.deepseek.com")

def generate_response_and_tts(question):
    # Generate text response
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        stream=False
    )

    # Extract text and generate TTS
    text = str(response.choices[0].message.content)
    wavs = chat.infer([text], use_decoder=True)

    # Save output audio file
    output_path = os.path.join(os.getcwd(), "output.wav")
    try:
        torchaudio.save(output_path, torch.from_numpy(wavs[0]).unsqueeze(0), 24_000)
    except:
        torchaudio.save(output_path, torch.from_numpy(wavs[0]), 24_000, format='wav')

    return text, output_path

def audio_player(audio_path):
    return Audio(audio_path)

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Text-to-Speech Demo")
    question = gr.Textbox(label="Your Question")
    text_output = gr.Textbox(label="Response")
    audio_output = gr.Audio(label="Generated Speech")

    def update_output(question):
        response_text, audio_path = generate_response_and_tts(question)
        return response_text, audio_path

    question.submit(update_output, inputs=question, outputs=[text_output, audio_output])

demo.launch()
