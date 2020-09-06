import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import operator
from cfg import config
import time
from utils import save_file, mark_link_crw, get_random_file_name


client = MongoClient()
db = client['web_crawler_db']
links_collection = db['Links']

while True:
    #getting links from database to crawl
    links= links_collection.find()

    print('links fetched')
    num_links = links_collection.count_documents({})

    if num_links>= config['max_links']:
        print('MAX LIMIT REACHED!!!!!!!')
        #ignore everything and continue

    print('No. of links found: ' + str(num_links))

    for link in links:
        #if link is crawled in the last 24 hours then
            #ignore everything and continue
        
        #if link is not crawled at all or it is not crawled in the last 24 hours then

            #do the web request
           
            print('making a web request')

            my_url = link['Link']
            r = requests.get(my_url)

            print('Link is ' + my_url)
            print('web request made')

            #if status code is not 200 then
            if r.status_code != 200:
                #mark link isCrawled = True and continue with next link
                mark_link_crw(link, r.status_code)
                continue

            print('Status code is 200')

            #find out the content type of response
            content_type = r.headers['content-type']

            if 'text/html' in content_type:
                #extract <a href= ""> links
                #save all links to database
                #save the file on disk
                save_file("","")
                #mark link isCrawled=True and continue with next link
                mark_link_crw(link, 200)
                continue

            #if content type is not html
                #Based on content type, create a file name
                get_random_file_name(content_type)

                #save the file on disk
                save_file("", "")
                #mark link isCrawled=True and continue with next link
                mark_link_crw(link, 200)
                continue




time.sleep(config['sleep_time'])