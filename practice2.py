#web scraper
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li',class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
skills =job.find('span',class_='srp-skills').text.replace(' ','')
published_date=job.find('span',class_='sim-posted').span.text
print(published_date)
"print(f'''
company_name: {company_name}
required_skills: {skills}

''')"








