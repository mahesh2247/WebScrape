# PYTHON SCRIPT USING BEAUTIFUL SOUP TO WEB SCRAP INTERNSHIP INFORMATION HOSTED AT INTERNSHALA.COM

from bs4 import BeautifulSoup

import requests

my_html = requests.get('https://internshala.com/internships/internship-in-bangalore').text

soup = BeautifulSoup(my_html, 'lxml')  # using lxml parser to scrap from webpage
jobs = soup.find_all('div', class_='internship_meta')  # identifying the DOM parent node
for job in jobs:
    company_name = job.find('a', class_='link_display_like_text').text
    domain = job.find('div', class_='heading_4_5 profile').text
    location = job.find('a', class_='location_link').text
    stipend = job.find('span', class_='stipend').text
    duration = job.find('div', class_='item_body').text
    print(f'''Company '{company_name.strip()}' which is situated in '{location.strip()}' relating to the domain = {domain.strip()} is offering internship for a duration of {duration.strip()} 
    for a stipend of {stipend.strip()}''')
    print(' ')









