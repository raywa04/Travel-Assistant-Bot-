
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def travel_assistant(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    user_input = "Can you help me book a flight to Paris?"
    print(travel_assistant(user_input))
