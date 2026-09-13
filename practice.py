import os
from dotenv import load_dotenv
from anthropic import Anthropic 

load_dotenv()

my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=my_api_key)

our_first_message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print(our_first_message.content[0].text)