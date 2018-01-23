import requests

def get_group_names(zendesk_instance):
    response = requests.get(zendesk_instance,auth=('sunjeet81@gmail.com','yorks64'),timeout = 1.00)
    
    if response.status_code != 200:
        print(f"Oops there has been a problem,instead of a 200 OK , {response.status_code} has been returned")
    else:
        print(response.status_code)
    json_response = response.json()
    print(json_response)
    print(json_response['groups'][0]['name'])
    groups = json_response['groups']
    with open('groups.txt',mode='w',encoding='utf-8') as file:
        for group in groups:
            print(group['name'])
            file.write(group['name']+'\n')
        
if __name__ == "__main__":
    get_group_names('https://sunjeet.zendesk.com/api/v2/groups.json')

    


