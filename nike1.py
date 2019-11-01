from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

csvFile = open("ReleaseInformation.csv","w",newline='')
writer = csv.writer(csvFile)
writer.writerow(["SneakerName","Colorway"])
url_1 = "https://www.nike.com/au/launch/"
html = urlopen(url_1).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
data = soup.find_all('a',{"aria-label":re.compile(r'(.*?)\sRelease\sDate')})

i_1=[]
i_2=[]
for a in data:
    a=(a['aria-label'])
    try:
        data_1 =re.search(r'(.*?)\s(\'.*\')\sRelease\sDate',a).group(1)
    except:
        data_1 = re.search(r'(.*?)\s(\'.*\')\sRelease\sDate', a)
    if data_1 == None:
        try:
            data_1 =re.search(r'(.*?)\sRelease\sDate', a).group(1)
        except:
            data_1 = re.search(r'(.*?)\sRelease\sDate', a)
    print(data_1)
    i_1.append(data_1)
    try:
        data_2 = re.search(r'(\'.*?\')', a).group(1)
    except:
        data_2 = re.search(r'(\'.*?\')', a)
    if data_2 == None:
        try:
            data_2 =re.search(r'(.*?)\sRelease\sDate', a).group(1)
        except:
            data_2 = re.search(r'(.*?)\sRelease\sDate', a)
    print(data_2)
    i_2.append(data_2)
    writer.writerows(zip([i_1[-1]],[i_2[-1]]))


