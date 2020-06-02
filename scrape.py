from bs4 import BeautifulSoup
import requests
import pprint


def main():
    links = []
    votes = []
    rank = []
    while True:
        try:
            page = int(input('How many pages of Hacker News would you like: '))
        except TypeError and ValueError:
            print('Provide an integer!')
        else:
            break
    for i in range(1, page + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')
        temp_links = soup.select('.storylink')
        temp_votes = soup.select('.score')
        temp_rank = soup.select('.rank')
        links += temp_links
        votes += temp_votes
        rank += temp_rank
    pprint.pprint(new_hn(links, votes, rank))


def new_hn(links, votes, rank):
    hn = []
    for idx, item in enumerate(links):
        post = int((votes[idx].getText()).replace(' points', ''))
        if post > 100:
            title = item.getText()
            href = item.get('href', None)
            hn.append({'Title': title, 'Link': href, 'Votes': post, 'Rank': rank[idx].getText().replace('.', '')})
    sort_hn = (sorted(hn, key=lambda temp: temp['Votes'], reverse=True))
    return sort_hn


if __name__ == '__main__':
    main()
