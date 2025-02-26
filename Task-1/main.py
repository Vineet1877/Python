import requests
import os

version = input("Enter version: ")

if requests.__version__ == version or version == "":
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    print(data)
else:
    os.system(f"python -m pip install requests=={version}")




