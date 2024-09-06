

# ChatTTS+LLM
# ChatTTS
[**English**](./README.md) | [**中文简体**](./README_CN.md)

The information in this document is for academic purposes only. It is intended for educational and research purposes and may not be used for any commercial or legal purpose. The author does not warrant the accuracy, completeness or reliability of the information. The information and data used in this document are for academic research purposes only. The data is derived from publicly available sources and the authors make no claim to ownership or copyright of the data.

ChatTTS is a powerful text-to-speech system. However, it is very important to use this technology responsibly and ethically. In order to limit the use of ChatTTS, we added a small amount of extra high-frequency noise during the training of the 4w hour model and suppressed the sound quality as much as possible in mp3 format to prevent criminals from using it for potential crimes. At the same time, we have trained the detection model internally and plan to open it in the future.
The LLM is the api used for my deepseek calls that can't be used when my token is used up
---
## Usage

<h4> Basic Usage </h4>
### Create a virtual environment

Second, enter the pytoch official website to find your cuda corresponding download
https://pytorch.org/get-started/locally/
### Change the directory
```python
cd lang_TTSLLM
```
### Download the dependencies I wrote

```python
pip install -r requirements.txt
```
### Finally run app.py

### If python app.py submits an error
```python
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## To get a gradio screen