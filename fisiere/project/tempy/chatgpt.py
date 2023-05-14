import openai

openai.api_key = "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"

prompt = "Write a short story about a robot and a human who become friends."

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.7,
)

print(response.choices[0].text)