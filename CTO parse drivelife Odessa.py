import re
import requests
import re
from bs4 import BeautifulSoup
pattern = r"(?:\+380)(?:\d{9})"
with open("CTO drivelife ivano-frankovsk.txt", 'a') as f:
    for p in range(1, 3):
        url = f'https://drivelife.org/ivano-frankovsk/sto?pages={p}'
        
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'lxml')
        all_CTO = soup.findAll('tr', class_="rowFinded0 ratingStars")
        for cto in all_CTO:
            tels = cto.find('a').get('title')
            result = re.findall(pattern, tels)
            for i in result:
                f.write((i)+'\n')
