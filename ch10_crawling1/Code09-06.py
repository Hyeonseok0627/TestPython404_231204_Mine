import bs4

# 초기세팅
#학원 pc
webPage = open('C:/TestPython/ch10_crawling1/Sample03.html',
               'rt', encoding='utf-8').read()

#집 pc(mac)
# webPage = open('/Users/hyeonseoklee/Desktop/IT Dev/Python_class/TestPython404_231204_Mine/ch10_crawling1/Sample03.html',
#                'rt', encoding='utf-8').read()

bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 각 태그의 속성 까지 포함해서 검색.
tag = bsObject.find('div', {'id': 'myId1'})
print(tag)

tag = bsObject.find('div', {'class': 'myClass1'})
print(tag)

# 복수로 찾을 시 리스트 화 해서 하는 부분.
tag = bsObject.findAll('div', {'class': 'myClass1'})
print(tag)
