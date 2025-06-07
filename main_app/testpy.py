import google.generativeai as genai

genai.configure(api_key="AIzaSyDliTjiJL0o3Gm0wQHerzy1Q5S4vvOG-oY")  # Replace with your actual key

models = genai.list_models()

for model in models:
    print(f"Model: {model.name} | Supported Methods: {model.supported_generation_methods}")
