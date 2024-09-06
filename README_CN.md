# ChatTTS
[**English**](./README.md) | [**中文简体**](./README_CN.md)

本文件中的信息仅供学术交流使用。其目的是用于教育和研究，不得用于任何商业或法律目的。作者不保证信息的准确性、完整性或可靠性。本文件中使用的信息和数据，仅用于学术研究目的。这些数据来自公开可用的来源，作者不对数据的所有权或版权提出任何主张。

ChatTTS是一个强大的文本转语音系统。然而，负责任地和符合伦理地利用这项技术是非常重要的。为了限制ChatTTS的使用，我们在4w小时模型的训练过程中添加了少量额外的高频噪音，并用mp3格式尽可能压低了音质，以防不法分子用于潜在的犯罪可能。同时我们在内部训练了检测模型，并计划在未来开放。
LLM是用于我的deepseek调用的api，当我token被用完后就无法是用来
---
## 用法

<h4>基本用法</h4>
### 创建一个虚拟环境

### 其次进入pytoch官网找自己cuda对应的下载
https://pytorch.org/get-started/locally/
### 切换目录
```python
cd lang_TTSLLM
```
### 下载我写好的依赖

```python
pip install -r requirements.txt
```

### 最后运行 app.py

### 运行出错
在requirements.txt里找 ctrl+F 找需要的model 用pip下载

### 如果python app.py 提交报错

```python
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## 即可获得一个gradio界面

