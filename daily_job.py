import os
from dotenv import load_dotenv
import db
import requests
import datetime
from bs4 import BeautifulSoup
import threading

# # create db
# load_dotenv()
# conn = db.db(os.getenv('HOST'), os.getenv('UUID'), os.getenv('DBNAME'), os.getenv('PASSWORD'))

# http request session
s = requests.Session()

# due day
start_date = datetime.date(2021, 6, 1)
end_date = datetime.date(2022, 6, 1)
delta = datetime.timedelta(days=1)



def getlink(s, date):
    data = {
        'title_type': 'feature',
        'release_date': date,
        'count': 250
    }

	#Get IMDB Path
    # https://www.imdb.com/search/title/?title_type=feature&release_date=2022-06-01&count=250
    # lister-item.mode-advanced

    response = s.post('https://www.imdb.com/search/title/?', data=data)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    formalist = soup.select('div.lister-item-content')
    mvlist = []
    for mv in formalist:
        header = mv.select_one('h3.lister-item-header a').getText()
        link = mv.select_one('h3.lister-item-header a').get("href")
        runtime = mv.select_one('span.runtime')
        if runtime != None:
            runtime = runtime.getText()
        else:
            runtime = 'Null'
        mvtype = mv.select_one('span.genre')
        if mvtype != None:
            mvtype = mvtype.getText().strip('\n').strip(' ')
        else:
            mvtype = 'Null'

        mvlist.append({'header': header, 'link': link, 'runtime': runtime, 'type': mvtype})
    return mvlist

def scrapToDatabase(movie):
    print(scrapToDatabase)

# movie list
movieList = []

# Main progress
def getLinkJob():
    global s
    global start_date
    global end_date
    global delta
    while start_date <= end_date:
        print('Getting ' + str(start_date) + ' IMDB movie data')
        movieList.extend(getlink(s, start_date))
        start_date += delta

# 建立一個子執行緒
t = threading.Thread(target = getLinkJob)
# 執行該子執行緒
t.start()
# 等待 t 這個子執行緒結束
t.join()


# for i in movieList:
#     scrapToDatabase(i)

print(len(movieList))