'''
Parse the response from the endpoint and print date and the high and low temperatures for the next 10 days in ChCh :) 
https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22christchurch%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys

'''
import requests

def get_max_min_temp(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Oops there has been a problem,instead of a 200 OK , {response.status_code} has been returned")
    else:
        print(response.status_code)
    json_response = response.json()
    print(json_response)
    results_list= json_response['query']['results']['channel']['item']['forecast']
    for item in results_list:
        print(f"The high of {item['date']} is {item['high']} Fahrenheit and the low for the day is {item['low']} fahrenheit ")
    
if __name__ == "__main__":
    get_max_min_temp('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22christchurch%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
