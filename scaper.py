import requests
from bs4 import BeautifulSoup

URL = "https://myanimelist.net/topanime.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content")

job_elements = results.find_all("tr", class_="ranking-list")

for job_element in job_elements:
    title_element = job_element.find("td", class_="rank")
    company_element = job_element.find("td", class_="title")
    
    location_element = job_element.find("td", class_="score")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text)
    print()

