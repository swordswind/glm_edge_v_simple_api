from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from transformers import AutoTokenizer, AutoImageProcessor, AutoModelForCausalLM
import torch
import base64
from io import BytesIO
from PIL import Image
import uvicorn

app = FastAPI()
print("正在加载GLM-Edge-V模型，请稍后...")
model_dir = "model/glm-edge-v-2b"
processor = AutoImageProcessor.from_pretrained(model_dir, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, torch_dtype=torch.bfloat16, device_map="auto",
                                             trust_remote_code=True)


@app.post("/glm_edge_v")
async def run_glm_edge_v(request: Request):
    data = await request.json()
    input_image_base64 = data['image']
    msg = data['msg']
    image_data = base64.b64decode(input_image_base64.split(",")[1])
    image = Image.open(BytesIO(image_data))
    messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": msg}]}]
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=True, tokenize=True,
                                           return_tensors="pt").to(next(model.parameters()).device)
    pixel_values = processor(image, return_tensors="pt").pixel_values.to(next(model.parameters()).device)
    generate_kwargs = {**inputs, "pixel_values": pixel_values}
    output = model.generate(**generate_kwargs, max_new_tokens=100)
    result = tokenizer.decode(output[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)
    return JSONResponse(content={"answer": result})


print("本地GLM-Edge-V模型API服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=8085)
