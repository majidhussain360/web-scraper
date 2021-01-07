#web scraper
from bs4 import BeautifulSoup
import requests
print('enter skills tht you are not familair with')
unfamiliar_skills=input(">")
unfamiliar_skill2=input(">")
unfamiliar_skill3=[unfamiliar_skills,unfamiliar_skill2]
print(f'filtering out{unfamiliar_skill3}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if "few"in published_date:
        company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills =job.find('span',class_='srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        if 'unfamiliar_skill3' not in skills:
            print(f'company_name: {company_name.strip()}')
            print(f'required_skilss: {skills.strip()}')
            print(f'more info: {more_info}')
            print('')








