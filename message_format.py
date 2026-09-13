from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client=Anthropic()

def translate(word, language):  
  response = client.messages.create(
      model="claude-sonnet-4-6",
      max_tokens=1000,
      messages=[
          {"role": "user", "content": f"Translate the word {word} into {language}. Only respond with the translated word, nothing else"}
      ]
  ) 

  print(response.content[0].text)

translate("boy", "Yoruba")