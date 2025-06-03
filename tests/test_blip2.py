from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch

# 使用基础配置加载（不需要 float16，也不需要 device_map）
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")


# 读取图像
image = Image.open("../backend/backend/static/placeholder_logo.png").convert("RGB")

# 提示词
prompt = (
    "A logo for"
)

# 输入处理
inputs = processor(images=image, text=prompt, return_tensors="pt")

# 生成 caption
generated_ids = model.generate(**inputs)
caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(caption)

# 提示词
prompt = (
    "The style"
)

# 输入处理
inputs = processor(images=image, text=prompt, return_tensors="pt")

# 生成 caption
generated_ids = model.generate(**inputs)
caption = processor.batch_decode(generated_ids[0], skip_special_tokens=True)
print(caption)


# prompt = (
#     "Describe this logo in detail: its main color and shape, any text it contains, "
#     "its style (e.g., modern, minimalist), and any unique visual elements."
# )