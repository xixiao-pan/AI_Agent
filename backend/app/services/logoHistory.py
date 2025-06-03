from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model="text-embedding-3-small") -> list:
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding

# 假设有以下 logo 描述
logo_descriptions = [
    {"id": "logo1", "text": "The logo features the word 'Chocolush' in a playful, cursive font. The main color is a creamy white for the text, outlined with a rich, chocolate brown, giving it a bold and appetizing look. The style is fun and whimsical, with a strong emphasis on chocolate-themed elements. Surrounding the text are various chocolate-related visuals, including pieces of chocolate bars, truffles, and nuts, adding a decorative touch. These elements are integrated into the outline, creating a cohesive and immersive design that highlights the brand's association with chocolate. The overall style is vibrant and engaging, appealing to a sense of indulgence and sweetness.."},
    {"id": "logo2", "text": " The logo features the text 'girl sheep' in a stylish, serif font. The main color of the background is a soft mint green. The 'g' is large and prominent, black in color, and has a whimsical curl at the top. Above the 'i' in girl, there is a pink circle with a black outline, resembling a stylized dot. Next to the 'l' in 'girl,' there is a small, simple line drawing of a sheep in black, adding a playful element. The overall style is modern with a touch of whimsy, combining a minimalist approach with unique, playful visual elements."},
    {"id": "logo3", "text": " The logo features a warm brown color, giving it an earthy and inviting feel. The central visual element is a stylized illustration of a chocolate bar, complete with two leaves and a cocoa pod, suggesting a natural and artisanal theme. The text Chocolush is written in a cursive, flowing script, adding an elegant and classic touch to the design. The overall style is a blend of modern and minimalist, with clean lines and a simple composition that emphasizes the product's natural origins. Unique visual elements include the integration of the chocolate bar with the leaves and pod, reinforcing the brand's connection to quality chocolate."}
]

# 用户输入
user_prompt = "I want to reference the previous logo surrounded by chocolate."

# 为每个 logo 和 prompt 生成 embedding
user_embedding = get_embedding(user_prompt)
logo_embeddings = [(logo["id"], get_embedding(logo["text"])) for logo in logo_descriptions]

# 计算相似度
similarities = [
    (logo_id, cosine_similarity([user_embedding], [embedding])[0][0])
    for logo_id, embedding in logo_embeddings
]

# 找到最相似的 logo
best_match = max(similarities, key=lambda x: x[1])
print(f"Best matched logo: {best_match[0]}, similarity: {best_match[1]:.3f}")