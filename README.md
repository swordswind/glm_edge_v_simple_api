# glm_edge_v_simple_api

## Project Overview

`glm_edge_v_simple_api` is an API server project for the GLM-Edge-V-2B multimodal large model developed by ZhiPu. The project aims to provide a fast and accurate image understanding and Q&A service, allowing users to integrate the multimodal large model into their applications through API calls, enabling intelligent Q&A functionality based on user-uploaded images.

## Project Addresses

- GitHub Project Address: [https://github.com/swordswind/glm_edge_v_simple_api](https://github.com/swordswind/glm_edge_v_simple_api)
- GLM-Edge Source Address: [https://github.com/THUDM/GLM-Edge](https://github.com/THUDM/GLM-Edge)
- GLM-Edge-V-2B Source Address: [https://modelscope.cn/models/ZhipuAI/glm-edge-v-2b](https://modelscope.cn/models/ZhipuAI/glm-edge-v-2b)

## Hardware Requirements

Ensure that your computer has an NVIDIA dedicated graphics card installed with a memory capacity of ≥6G.

## Server Address

The API server address for the GLM-Edge-V large model is: `http://your_computer_IP:8085/`

## API Interface

### Interface Address

`/glm_edge_v`

### Request Method

POST

### Request Parameters

The request body content is in JSON format, including the following fields:

- `image`: Base64 encoded image data, in string format. The image prefix must be included, for example: `data:image/png;base64,`
- `msg`: The text information input by the user, in string format, is a question about the image.

## Usage Example

For example client code, please refer to `vlm_test_client.py`.

### Testing Method

1. Run "python vlm_test_client.py" to perform a usage test.
2. You can customize and replace the `demo.jpg` sample image.

## Precautions

1. It is recommended to use an NVIDIA dedicated graphics card with a memory capacity of ≥6G when running this API server (it can also run slowly on a CPU only).
2. This API server only supports the POST request method.

## Dependency Installation

Install project dependencies through the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Quick Start

1. Start the API server:

   ```bash
   python api.py
   ```

2. Test the API with a client:

   ```python
   import requests
   import base64
   
   def call_vlm_api():
       with open("demo.jpg", "rb") as image_file:
           base64_image = base64.b64encode(image_file.read()).decode('utf-8')
       data = {"image": f"data:image/jpeg;base64,{base64_image}", "msg": "Describe this picture in detail"}
       response = requests.post("http://127.0.0.1:8085/glm_edge_v", json=data)
       return response.json()
   
   
   while True:
       input("Press any key to start GLM-Edge-V testing")
       print("Test command sent, waiting for VLM response...")
       try:
           result = call_vlm_api()
           print(result)
       except:
           print("Note: Please run the VLM model API server first, then use the client to test VLM.")
   ```

## Contribution

Contributions to the project are welcome, including but not limited to:

- Code optimization
- New feature development
- Bug fixing

## License

This project is licensed under the [MIT](LICENSE) license.
