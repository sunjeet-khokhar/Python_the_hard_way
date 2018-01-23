import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY',timeout = 1.00)

if response.status_code != 200:
    print(f"Oops there has been a problem,instead of a 200 OK , {response.status_code} has been returned")
else:
    print(response.status_code)
json_response = response.json()
print(json_response)
picture_title = json_response['title']
print(picture_title)
with open('title.txt',mode='w',encoding='utf-8') as file:
    file.write(picture_title)





