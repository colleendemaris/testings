import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import shutil

def txtdownload():
    url = 'http://web.mta.info/developers/turnstile.html'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    all_a_links = soup.findAll('a')     #this grabs EVERYTHING with a

    one_a_tag = soup.findAll('a')[36]  #this grabs one single a tag

    link = one_a_tag['href']            #this turns it from an a tag to a link

    download_url = "http://web.mta.info/developers/" + link

    #urllib.request.urlretrieve is the command to download the file in a href
    #add the download url
    #turnstile is the start of the name
    urllib.request.urlretrieve(download_url, './’'+ link[link.find('/turnstile_')+1:])

def imgdownload():
    url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
    
    html = urlopen(url)

    bs = BeautifulSoup(html, "html.parser")

    images = bs.find_all('img', {'src':re.compile('.jpg')})

    name = "name0"

    for image in images:
        image_url = "http://" + image['src'][2:]
        
        resp = requests.get(image_url, stream=True)
        local_file = open(name + '.jpg', 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        name = name + "0" #replace this with a name function

def textdownload():
    url = 'https://www.learnreligions.com/papa-legba-4771384'

    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    # titles = soup.findAll('h3') #this also works for just all h3 elements
    titles = soup.findAll('h3', attrs={'class': 'comp mntl-sc-block mntl-sc-block-heading'})

    for name in titles:
        title = name.text.strip()
        print(title)

textdownload()