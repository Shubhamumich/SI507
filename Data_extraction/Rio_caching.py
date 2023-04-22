import requests
from bs4 import BeautifulSoup
import json
import re
import os




json_file = "Riotrial.json"

if os.path.exists(json_file):
    with open(json_file, "r") as file:
        winner_data = json.load(file)
else:
    url = "https://olympics.com/en/olympic-games/rio-2016/results/swimming"
    response = requests.get(url, headers={'User-Agent': "Mozilla/5.0"})
    print(response.status_code)   
    response_code = response.status_code
    if  response_code != 200:
        print("Error Occured")


    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')

    # categories = [category.text for category in soup.select("div.hgxeXK h2")]

    winner_data = []
    sections = soup.find_all("section", {"class": "bDlpVX"})
    for section in sections:

        categories = section.find_all('h2', class_='hdLbhC')[0].text
        
        
        
        results = section.find_all('div', class_='zvSuQ')
        for result in results:
            winners = result.find_all('div', class_='uCYN')
            for winner in winners:
                #print('\t')
                try:
                    name = winner.find_all('a', class_='btmbqi')[0].text
                    #print(name)
                except:
                    name = "Multiple Winners"
                    #print(name)
                medal = winner.find_all('span', class_='cpcCbi')[0].text
                #print(medal)
                
                if name == "Multiple Winners":
                    try:
                        country = winner.find_all('div', class_='bfgpvV')[0].text
                        #print(country)
                    except:
                        country = winner.find_all('span', class_='bojjbG')[0].text
                        #print(country)
                        
                else:    
                    country = winner.find_all('span', class_='bojjbG')[0].text
                    #print(country)
                print('\n')
                
                
                winner_data.append({
                    "category": categories,
                    "name": name,
                    "medal": medal,
                    "country": country
            
                    })
                print(winner_data)

    
            with open("Riotrial.json", "w") as outfile:
                json.dump(winner_data, outfile, indent=4)