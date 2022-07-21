import os
from dotenv import load_dotenv
import db
import requests
import datetime
from bs4 import BeautifulSoup
import threading
import time
start = time.time()
# # create db
# load_dotenv()
# conn = db.db(os.getenv('HOST'), os.getenv('UUID'), os.getenv('DBNAME'), os.getenv('PASSWORD'))

# http request session
s = requests.Session()

# due day
start_date = datetime.date(2022, 6, 1)
end_date = datetime.date(2022, 6,2)
delta = datetime.timedelta(days=1)



def getlink(s, date):
    print('getlink' + str(date))
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
def getLinkJob(s, date):
    global movieList
    print('Getting ' + str(date) + ' IMDB movie data')
    movieList.extend(getlink(s, date))
    print('done ')

# Get movie data in detail page and merge data
def getDetailJob(s, mv):
    mvinfo = {}
    mvdetail = s.post('https://www.imdb.com' + mv['link'])
    res = mvdetail.text
    mvsoup = BeautifulSoup(res, "html.parser")
    actorlist = mvsoup.select('a.sc-36c36dd0-1')
    characterlist = mvsoup.select('span.sc-36c36dd0-4')
    information = mvsoup.select('div.sc-388740f9-0')
    actors = []
    characters = []
    for name in actorlist:
        actor = name.getText()
        actors.append(actor)
    for name2 in characterlist:
        character = name2.getText()
        characters.append(character)
    mvinfo['title'] = mv['header']
    mvinfo['id'] = mv['link']
    mvinfo['poster'] = mvsoup.select_one('div.ipc-media img').get('src')
    mvinfo['trailer'] = 'https://www.imdb.com' + mvsoup.select_one('div.ipc-slate a').get('href')
    if not mvinfo['trailer'].__contains__('https://www.imdb.com/video'):
        mvinfo['trailer'] = 'Null'
    mvinfo['runtime'] = mv['runtime']
    mvinfo['actors'] = actors
    mvinfo['characters'] = characters
    mvinfo['storyline'] = mvsoup.select_one('span.sc-16ede01-2').getText()
    #mvinfo['storyline2'] = information.select_one('div.ipc-html-content-inner-div').getText()
    # mvinfo['releaseDate'] = str(date)
    # ...

    #print(mvinfo['characters'])
    print(mvinfo)

threads = []
while start_date <= end_date:
  threads.append(threading.Thread(target = getLinkJob, args = (s, start_date)))
  threads[-1].start()
  start_date += delta
  time.sleep(1)

# 等待所有子執行緒結束
for t in threads:
  t.join()

detailThreads = []
for i in movieList:
    detailThreads.append(threading.Thread(target = getDetailJob, args = (s, i)))
    detailThreads[-1].start()
    time.sleep(1)

# 等待所有子執行緒結束
for t in detailThreads:
  t.join()

print(len(threads), " days")
print(len(detailThreads), " movies")
end = time.time()
print('time count ', end - start)