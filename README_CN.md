# glm_edge_v_simple_api
## 项目简介
`glm_edge_v_simple_api` 是一个基于智谱开发的 GLM-Edge-V-2B 多模态大模型的 API 服务器项目。该项目旨在提供一个快速、准确的图像理解和问答服务，允许用户通过 API 调用将多模态大模型集成到他们的应用程序中，实现基于用户上传图像的智能问答功能。

## 项目地址
- GitHub 项目地址：[https://github.com/swordswind/glm_edge_v_simple_api](https://github.com/swordswind/glm_edge_v_simple_api)
- GLM-Edge源地址：[https://github.com/THUDM/GLM-Edge](https://github.com/THUDM/GLM-Edge)
- GLM-Edge-V-2B源地址：[https://modelscope.cn/models/ZhipuAI/glm-edge-v-2b](https://modelscope.cn/models/ZhipuAI/glm-edge-v-2b)
## 硬件需求

确保你的计算机安装了 NVIDIA 独立显卡，且显存≥6G。

## 服务器地址
GLM-Edge-V大模型API服务器地址为：`http://你的电脑IP:8085/`
## API接口
### 接口地址
`/glm_edge_v`
### 请求方式
POST
### 请求参数
请求体内容为 JSON 格式，包含以下字段：
- `image`：Base64 编码的图像数据，格式为字符串。必须包含图像前缀，例如：`data:image/png;base64,`
- `msg`：用户输入的文本信息，格式为字符串，是对图像的提问。
## 使用示例
示例客户端代码请查看 `vlm_test_client.py`。
### 测试方式

1. 运行“python vlm_test_client.py”即可进行使用测试。
2. 可自定义更换 `demo.jpg` 示例图片。

## 注意事项
1. 运行本API服务器推荐使用显存≥6G的NVIDIA独立显卡(纯CPU也可缓慢运行)。
2. 本API服务器仅支持POST请求方式。
## 依赖安装

通过 `requirements.txt` 文件安装项目依赖：

```bash
pip install -r requirements.txt
```

## 快速开始

1. 启动 API 服务器：

   ```bash
   python api.py
   ```

2. 使用客户端测试 API：

   ```python
   import requests
   import base64
   
   def call_vlm_api():
       with open("demo.jpg", "rb") as image_file:
           base64_image = base64.b64encode(image_file.read()).decode('utf-8')
       data = {"image": f"data:image/jpeg;base64,{base64_image}", "msg": "详细描述这张图片"}
       response = requests.post("http://127.0.0.1:8085/glm_edge_v", json=data)
       return response.json()
   
   
   while True:
       input("按任意键开始GLM-Edge-V测试")
       print("测试指令已发送，等待VLM回答...")
       try:
           result = call_vlm_api()
           print(result)
       except:
           print("提示: 请先运行VLM模型API服务器，再使用客户端进行VLM测试。")
   ```

## 贡献

欢迎对项目进行贡献，包括但不限于：
- 代码优化
- 新功能开发
- 问题修复
## 许可证
本项目采用 [MIT](LICENSE) 许可证。
