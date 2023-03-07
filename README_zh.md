#OpenAI API插件
**OpenAIApi插件**让您可以访问**虚幻引擎**中的**OpenAI API**。它与UE4.26、4.27、5.0和最新版5.1兼容


这是一个社区插件。与OpenAI没有关联。


##安装


安装插件的推荐方法是使用预构建的二进制文件。




-下载插件[这里]（https://drive.google.com/drive/folders/16FFYDf0U--nxUocQVXCIvSo-Sa0Tnndl?usp=sharing）
-在您的项目文件夹下创建一个“Plugins”的文件夹
-将插件复制到其中，这样您就有了“YourProject/Plugins/OpenAIAPI”


##快速启动


见[视频]（https://www.youtube.com/watch?v=hUv2_gis_9I）


[！[]（http://img.youtube.com/vi/hUv2_gis_9I/0.jpg）]（http://www.youtube.com/watch?v=hUv2_gis_9I《OpenAI API快速入门教程》）


>**注意**：此视频在不断更新，向您展示如何使用DALL·E 2在“虚幻引擎”中生成图像。 


##鉴权类型
有两种方法可以设置Api Key
-直接在蓝图中分配Api密钥。


-将Api Key设置为环境变量




！[]（https://i.imgur.com/HF2tdBz.png）
>**建议**：在打包之前要注意安全并加密您的资产。




！[]（https://i.imgur.com/0fpPVlV.png）
>**ADVICE**：创建环境变量'OPENAI_API_KEY'并使用您的api键作为值。




##蓝图节点
####OpenAI调用GPT3，GPT3.5


-此异步节点使用您的引擎、提示符和设置发送HTTP请求。


！[]（https://i.imgur.com/vGo2wta.png）
>**注意**：此节点只能从蓝图的“事件图”中调用。 
####进行设置


-此节点允许您设置请求正文参数。


！[]（https://i.imgur.com/xS4MMrI.png）
>**注意**：额外参数“开始序列”在提示的开头注入文本。
>
>'log_probs'和'stream'在未来支持
####中断完成


-此节点用于访问“完成”或“选择”中包含的值


！[]（https://i.imgur.com/dydM8Sd.png）
当前不支持log_probs。
##用法
此示例显示了在蓝图中实现的OpenAI聊天示例。


！[]（https://i.imgur.com/DNKp0bW.png）


此示例显示如何在蓝图中使用DALL·E 2生成1024x1024图像。


！[]（https://i.imgur.com/CciUUF6.png）


##引用
-[OpenAI的API引擎文档]（https://beta.openai.com/docs/engines）
-[OpenAI的API参考]（https://beta.openai.com/docs/api-reference/completions）
-[Chatgpt的API参考]（https://chat.openai.com/chat）


##支持的平台
Windows 
Mac 
Android 

##其他调用
adapters:
  - ws
debug: true
enableVerify: true
verifyKey: kemomi
singleMode: false
cacheSize: 1086
adapterSettings:
  ws:
    host: localhost
    port: 8080
    reservedSyncId: -1
