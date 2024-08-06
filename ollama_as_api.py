import requests
import json

url = "http://localhost:11434/api/generate"
payload = json.dumps({
  "model": "gemma2:2b",
  "prompt": "Hello my name is Othman Samih",
  "stream": False
})

response = requests.post(url, data=payload)
print(response.json()['response'])
