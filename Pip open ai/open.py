import openai
openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = str(input("Enter your prompt: "))
completion = openai.Completion.create(
engine=model_engine,
prompt=prompt,
max_tokens = 1024,
n=1,
stop=None,
temperature=0.9,
)
response = completion.choices[0].text
print(response)