import openai

openai.api_key = "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"

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = generate_response(user_input)
    print("Chatbot:", response)