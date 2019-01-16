from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import re
urls = ('https://myams.org/clubs-directory/page/{}/'.format(i) for i in range(1,100))
driver = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')
driver.maximize_window()
iii=0
end=0
datas=[]
for url in urls:
    driver.get(url)
    data = driver.page_source
    soup = BeautifulSoup(data, 'lxml')
    titlesEntries = soup.find_all(class_='entry-title')
    for titlesEntry in titlesEntries:
        tag=str(titlesEntry.contents[0])
        #titlesEntry.next_siblings
        clas=repr(titlesEntry.next_element.next_element.next_element)
        dr=re.compile(r'<[^>]+>',re.S)
        text=dr.sub('',tag)
        clasText=dr.sub('',clas)
        clasText=clasText.replace('&amp;','&')
        if ("Clubs Directory" not in text):
            iii+=1
            print('第'+str(iii)+"个标题"+text+'   分类'+clasText)
            datas.append([text,clasText])
            end=0
        else:
            end+=1
        if end>=2:
            with open('clubs-directory.csv', 'w', newline='',encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                for row in datas:
                    writer.writerow(row)
            exit()
