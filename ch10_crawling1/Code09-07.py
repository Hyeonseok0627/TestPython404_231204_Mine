import bs4

# 초기세팅
#학원 pc
# webPage = open('C:/TestPython/ch10_crawling1/Sample03.html',
#                'rt', encoding='utf-8').read()

#집 pc(mac)
webPage = open('/Users/hyeonseoklee/Desktop/IT Dev/Python_class/TestPython404_231204_Mine/ch10_crawling1/Sample03.html',
               'rt', encoding='utf-8').read()

bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

ul_value = bsObject.find('ul', {'class': 'myClass2'})
print(ul_value)

li_list = bsObject.findAll('li', {'class': 'myClass3'})
print(li_list)
