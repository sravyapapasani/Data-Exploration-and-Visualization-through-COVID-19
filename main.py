from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
country=[] 
active_cases=[] 
deaths=[] 
vaccinated=[]
driver.get("https://covid19.who.int/table")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
countries=a.find('div', attrs={'class':'_3wU53n'})
cases=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
vaccinated=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
death=a.find('div', attrs={'class':'iMSR67'})
country.append(countries.text)
active_cases.append(cases.text)
deaths.append(death.text) 
vaccinated.append(vaccinated.text)
df = pd.DataFrame({'Country':country,'Active cases':active_cases,'Deaths':deaths,'Vaccinated people':vaccinated}) 
df.to_csv('covid_cases.csv', index=False, encoding='utf-8')
