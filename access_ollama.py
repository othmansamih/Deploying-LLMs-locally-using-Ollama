import ollama
import time

time_start = time.time()
stream = ollama.chat(
    model='mymodel:latest',
    messages=[{'role': 'user', 'content': 'What is Machine Learning?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

time_end = time.time()
print(f"Time of execution is: {time_end-time_start}")