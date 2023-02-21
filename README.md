# UE-chatgpt
基于UE5引擎实现与ai聊天，融合了chatgpt-3，VITS语音合成，NLP情感分析。自定义给予ai角色设定，项目仍在开发完善中 谢谢大家！  

本项目：https://github.com/kemomi/UE-chatgpt

# Unreal Engine Plugin---UE-chat

一个虚幻引擎插件，通过添加相关chatapi接口来通过异步任务执行识别和合成，将chatgpt自然语言认知服务集成到引擎中。
--------------------------------------------

# 使用虚幻引擎（Unreal Engine）创建一个ChatGPT插件，按照以下步骤进行操作：

1.首先，您需要安装Python和TensorFlow等必要的工具来运行ChatGPT模型并生成响应。确保您的Python和TensorFlow版本与您要使用的ChatGPT模型兼容。

## 安装必要的软件和依赖项

确保您的系统上安装了Python和TensorFlow，以及其他所需的软件和依赖项。可以使用pip包管理器安装这些软件和依赖项

Python＞17

```python
pip install tensorflow
pip install transformers
```
## 下载ChatGPT模型
```sh
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = GPT2LMHeadModel.from_pretrained("microsoft/DialoGPT-medium")
```
## 定义生成响应的函数
使用TensorFlow和ChatGPT模型定义一个生成响应的函数。例如，下面是一个简单的函数，它使用ChatGPT模型生成给定输入的响应：
```python
def generate_response(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='tf')
    # Generate response using model
    output = model.generate(input_ids, max_length=1000, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
```
这个函数使用Tokenizer将输入文本编码成模型可以理解的格式，然后使用GPT2LMHeadModel生成一个响应，最后使用Tokenizer将响应解码成自然语言文本。

## 运行代码并生成响应
```python
input_text = "Hi, how are you?"
response = generate_response(input_text, model, tokenizer)
print(response)
```
在调用generate_response函数时，将输入文本传递给函数，以生成一个响应


2.接下来，您需要创建一个新的虚幻引擎项目。在创建项目时，确保选择支持Python插件的选项。这将使您能够在虚幻引擎中编写Python代码。

3.在您的项目中，创建一个新的Python插件。这将是您在其中实现ChatGPT逻辑的地方。您可以使用Python插件与虚幻引擎中的其他组件进行通信，UI元素和游戏世界。

4.在您的Python插件中，加载您的ChatGPT模型并设置其参数。这可能涉及到从磁盘加载模型文件，指定生成响应的长度，以及任何其他必要的设置。

5.编写代码来处理用户输入，并使用您的ChatGPT模型生成响应。这可能涉及到将用户输入格式化为模型可以理解的方式，将其转换为TensorFlow张量。
您还需要调用模型以生成响应，并将其返回给用户。

6.您需要将您的Python插件与虚幻引擎中的其他组件进行集成。这可能包括将您的插件与UI元素连接起来，以便用户可以与ChatGPT进行交互，或将您的插件与虚幻引擎中的其他系统进行交互，例如触发事件或改变游戏状态。

7.在您的插件中添加必要的UI元素，例如文本框、按钮等，以便用户可以与ChatGPT进行交互。您需要使用虚幻引擎的UMG（Unreal Motion Graphics）系统创建这些UI元素，并将它们与您的Python插件中的逻辑代码进行连接。

8.添加一些额外的逻辑代码来处理用户输入和响应。可能需要对用户输入进行一些预处理，例如去除标点符号和停用词，以使ChatGPT能够更好地理解用户的意图。

9.添加一些逻辑代码来处理响应，例如选择最有可能的响应，或使用一些NLG（Natural Language Generation）技术对响应进行后处理。

10.使用一些调试技术，例如打印日志或使用虚幻引擎的调试工具来检查您的代码中的错误。确保测试您的插件并在必要时进行调试。

最后，在您的Python插件中实现一些错误处理逻辑，以便能够在ChatGPT模型或虚幻引擎中出现错误时进行适当的处理。例如，您可以在模型出现错误时返回默认响应，或在虚幻引擎中出现错误时显示错误消息。
------------------------------------------

# Links
创建一个成功的ChatGPT插件，您需要有一些编程经验和对虚幻引擎的熟悉程度，以便将您的Python逻辑与虚幻引擎的其他系统进行集成。
同时，您需要具备一定的自然语言处理（NLP）和机器学习（ML）知识，以便能够设计和实现一个高效的ChatGPT模型。
总的来说，创建一个ChatGPT插件需要一定的技术知识和经验，但虚幻引擎的文档和社区可以提供帮助和支持。

虚幻引擎官网：
https://www.epicgames.com/store/zh-CN/

插件商店：
https://www.unrealengine.com/marketplace/en-US/store

UMG（Unreal Motion Graphics）：
https://docs.unrealengine.com/4.27/zh-CN/InteractiveExperiences/UMG

Chatgpt：
https://chat.openai.com/chat

OpenAI：
https://openai.com/research/natural-language-generation/

NLG（Natural Language Generation）：
https://www.nlgresources.org

Textio：
https://textio.com/
