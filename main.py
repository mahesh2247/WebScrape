# PYTHON SCRIPT USING BEAUTIFUL SOUP TO WEB SCRAP INTERNSHIP INFORMATION HOSTED AT INTERNSHALA.COM

from bs4 import BeautifulSoup
from re import search
import requests


def callscrap():
    my_dict = {}
    my_list = []
    my_html = requests.get('https://internshala.com/internships/internship-in-bangalore').text

    soup = BeautifulSoup(my_html, 'lxml')  # using lxml parser to scrap from webpage
    jobs = soup.find_all('div', class_='internship_meta')  # identifying the DOM parent node
    for job in jobs:
        company_name = job.find('a', class_='link_display_like_text').text
        domain = job.find('div', class_='heading_4_5 profile').text
        location = job.find('a', class_='location_link').text
        stipend = job.find('span', class_='stipend').text
        duration = job.find('div', class_='item_body').text
        my_dict['company_name'] = company_name.strip('\n ')
        my_dict['domain'] = domain.strip('\n ')
        my_dict['location'] = location
        my_dict['stipend'] = stipend.strip(' ')
        my_dict['duration'] = duration.strip('\n\xa0 ')
        my_list.append(my_dict)
        my_dict = {}
        print(f'''Company '{company_name.strip()}' which is situated in '{location.strip()}' relating to the domain = {domain.strip()} is offering internship for a duration of {duration.strip()} 
        for a stipend of {stipend.strip()}''')
        print(' ')

    print("JSON format   ")
    print(my_list)

    place = input('Enter any particular place of interest you are looking for an internship')
    print("PRINTING ALL THE COMPANY NAMES THAT OFFER AN INTERNSHIP IN {}".format(place))  # Filtering out JSON search based on location
    for i in range(len(my_list)):
        if my_list[i]['location'] == place:
            print(my_list[i]['company_name'])

    expected = int(input('Enter expected stipend'))  # Filtering out results from JSON based on stipend input from user
    print(" ")
    print('Companies offering internships in the expected stipend of - {}'.format(expected))
    print(" ")
    for i in range(len(my_list)):
        if search('-', my_list[i]['stipend']):  # Filtering out stipends with range
            ans = my_list[i]['stipend'].find('-')
            if ans != -1:
                maxi, mini = my_list[i]['stipend'].strip(' /monthlumpsum').split('-')
                maxi = int(maxi)
                mini = int(mini)
                # print('{}  {}'.format(maxi, mini))
                if maxi <= expected <= mini:
                    print(my_list[i]['company_name'])
        else:
            s = my_list[i]['stipend'].strip(' /monthlumpsum+Incentive')  # Stripping some stipend strings that contain extra strings like incentives,+ and lumpsum
            s = int(s)
            if s == expected:
                print(my_list[i]['company_name'])


if __name__ == "__main__":
    callscrap()










