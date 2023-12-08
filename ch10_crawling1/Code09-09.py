import bs4

#학원 pc
# webPage = open('C:/TestPython/ch10_crawling1/Sample03.html',
#                'rt', encoding='utf-8').read()

#집 pc(mac)
webPage = open('/Users/hyeonseoklee/Desktop/IT Dev/Python_class/TestPython404_231204_Mine/ch10_crawling1/Sample03.html',
               'rt', encoding='utf-8').read()

bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_li_all = bsObject.findAll('li')

for tag_li in tag_li_all:
    # 태그를 제외하고 해당 텍스트 속성만 출력하기.(li 태그 안에 텍스트만 가져오는 코드)
    print(tag_li.text)
print()
for i in range(len(tag_li_all)):
    print(tag_li_all[i].text)
