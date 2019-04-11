import re

import bs4
import requests


def main():
    response = requests.get('https://tw.appledaily.com/new/realtime')
    # print(response.text)
    
    doc = bs4.BeautifulSoup(response.text, 'html.parser')
    p = doc.select('ul.rtddd > li.rtddt') # 往下找一層
    # p = doc.select('li.rtddt, h1.r>a')
    # print(len(p))

    popular = 0

    for result in p:
        # print(result)
        time = result.select_one('a > time')
        link = result.select_one('a')
        category = result.select_one('a > h2')
        header = result.select_one('a > h1')
        #popular = result.select_one('a, h1 > span')
        match = re.search(r'(?P<name>.+)(\((?P<read>\d+)\))', header.get_text())
        try:
            header = match.group('name')
            popular = int(match.group('read'))
        except AttributeError:
            header = header.get_text()

        print('時間: %s' % (time.get_text()))
        print('連結: %s' % (link.get('href')))
        print('-'*5)
        print('分類: %s' % (category.get_text()))
        print('標題: %s' % (header))
        print("人氣: %s" % (popular))
        print('-'*10)


if __name__ == "__main__" :
    main()