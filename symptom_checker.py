from openai import OpenAI
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="My API Key",
)

response = client.chat.completions.create(
  model="gpt-4",
  messages=[],
  temperature=0,
  max_tokens=1024
)