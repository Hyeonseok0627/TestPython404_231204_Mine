import bs4
# 실제 사이트에 접근하기 전에,
# 임시 html에서, 각 태그별 접근 연습.
#학원 pc
# webPage = open('C:/TestPython/ch10_crawling1/Sample02.html',
#                'rt', encoding='utf-8').read()

#집 pc(mac)
webPage = open('/Users/hyeonseoklee/Desktop/IT Dev/Python_class/TestPython404_231204_Mine/ch10_crawling1/Sample02.html',
               'rt', encoding='utf-8').read()

bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)
