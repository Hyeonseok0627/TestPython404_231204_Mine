import bs4

# 초기세팅
#학원 pc
webPage = open('C:/TestPython/ch10_crawling1/Sample02.html',
               'rt', encoding='utf-8').read()

#집 pc(mac)
# webPage = open('/Users/hyeonseoklee/Desktop/IT Dev/Python_class/TestPython404_231204_Mine/ch10_crawling1/Sample02.html',
#                'rt', encoding='utf-8').read()

bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 데이터 가져오기 연습
tag_ul = bsObject.find('ul')
print(tag_ul)
print()

tag_li = bsObject.find('li')
print(tag_li)
print()

# 복수개를 찾아서 , 리스트에 담아서 작업.
tag_li_all = bsObject.findAll('li')
print(tag_li_all)
