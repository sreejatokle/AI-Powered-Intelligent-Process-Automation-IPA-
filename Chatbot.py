import openai

openai.api_key = 'your-openai-api-key'

# Chatbot function to interact with the user
def chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "gpt-4"
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example of chatbot interaction
user_input = "How can I reset my password?"
response = chatbot_response(user_input)
print("Chatbot Response:", response)
