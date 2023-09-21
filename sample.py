import requests

request = requests.get("https://fastapi-project-dun.vercel.app/")
print(request.json())
