from gpt4all import GPT4All
from app.prompt import get_prompt

# создаём модель
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # скачивается автоматически

def ask_ai(prompt: str) -> str:
    with model.chat_session():
        print(model.generate(prompt, max_tokens=306))




prompt = get_prompt("English", "Привет")
