# @ author Devang Sharma
# Searches for best hotels based on a place
import requests
from bs4 import BeautifulSoup
import re
import pprint


def main():
    main_list = []
    place = input('Enter a place: ')
    # Connecting to the airbnb website
    res = requests.get(f'https://www.airbnb.com/s/{place}/homes')
    # Getting the html of the airbnb website
    soup = BeautifulSoup(res.text, 'html.parser')
    # Selecting the titles of all the hotels
    titles = soup.select('._i24ijs')
    for item in titles:
        # Getting the page for each hotel to get some additional info
        temp_loc = location(item['href'].lstrip('/rooms/'))
        res2 = requests.get(f'https://www.airbnb.com/rooms/{temp_loc}')
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        temp_rating = soup2.find_all('div')
        rating = 0
        # Getting the ratings of the hotel
        for i in temp_rating:
            temp = re.search('.[r][e][v][i][e][w][s][)]$', i.getText())
            if i.attrs.get('dir') == 'ltr' and temp:
                rating = float(i.getText().split()[0])
        main_list.append({'Name': item['aria-label'], 'Rating': rating})
    # Sorting based on ratings
    return sorted(main_list, key=lambda x: x['Rating'], reverse=True)


def location(string):
    temp_loc = ''
    for i in string:
        if i.isnumeric():
            temp_loc += i
        else:
            return temp_loc


if __name__ == '__main__':
    pprint.pprint(main())
