from bs4 import BeautifulSoup as bs
import requests
import sys


def next_page(link, lst):
    print('link = https://en.wikipedia.org' + link)
    r = requests.get('https://en.wikipedia.org' + link)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        if r.status_code == 404:
            exit("It's a dead end !")
    soup = bs(r.text, 'html.parser')
    body = soup.find('div', {'class': 'mw-body-content mw-content-ltr'}).find_all('p')
    title = soup.find('span', {'class': 'mw-page-title-main'}).string
    print(body)
    next_link = body.find('div', {'class': 'mw-parser-output'}).find('p', {'class': None}).a
    print(next_link)
    if next_link['href'].startswith('/wiki/Help:') or next_link.startswith('/wiki/Wikipedia:'):
        # while str(next_link.parent)[0:3] != '<p>':
        next_link = next_link.find_next('a')
    # try:
    #     if next_link['class']:
    #         next_link = next_link.find_next('a')
    # except KeyError:
    #     pass
    # while str(next_link.parent)[0:3] != '<p>':
    #     next_link = next_link.find_next('a')
    print(title)
    print(next_link['href'])
    lst.append(title)
    if lst.count(title) > 1:
        exit('It leads to an infinite loop!')
    # print('next_link = ' + str(next_link))
    if title != 'Philosophy':
        next_page(next_link['href'], lst)



if __name__ == '__main__':
    sys.argv.append('reason')#('physics')
    lst = []
    next_page('/wiki/' + sys.argv[1].replace(' ', '_'), lst)
    for i in lst:
        print(i)
    print(len(lst), 'roads from', lst[0], 'to', lst[-1])
