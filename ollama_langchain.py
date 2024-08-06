from langchain_community.llms import Ollama
import time

start_time = time.time()
llm = Ollama(model="gemma2:2b")
response = llm.invoke("Hello my name is Othman Samih")
end_time = time.time()
print(response)
print(f"Execution time is: {end_time-start_time}")