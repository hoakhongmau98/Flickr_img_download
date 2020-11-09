from bs4 import BeautifulSoup
import os
import urllib.request
import requests
# source = urllib.request.urlopen("https://www.flickr.com/photos/trongveostudio/albums", "lxml.parser")
file_name = input('Put Your file name(html file require in /html):\n')
html_doc = open('html/'+file_name, mode='r')
soup = BeautifulSoup(html_doc)
# print(soup.title.string)
auth_dir = soup.title.string
try:
    os.mkdir('img')
except:
    None
try:
    os.mkdir('html')
except:
    None
try:
    os.mkdir('img/' + soup.title.string)
except:
    None
album_div = soup.find_all('a', class_="overlay")
# /content/gdirve/My Drive/Colab Notebooks/flickr


def get_id_img(link_album, auth_dir):
    # link_album = "https://www.flickr.com/photos/trongveostudio/albums/72157712813955698"
    # atract web to get the first id img
    link_text = link_album.split('/')
    source = urllib.request.urlopen(link_album)
    soup = BeautifulSoup(source)
    print(soup.title.string)
    album_name = soup.title.string
    # save web to html
    file_name = 'html/'+album_name+'.html'
    try:
        os.mkdir('img/'+auth_dir+'/'+album_name)
    except:
        None
    direct = 'img/'+auth_dir+'/'+album_name
    # show only div
    div_list = soup.find_all('div', class_='view photo-list-photo-view requiredToShowOnServer awake')
    # cut style from div to get id_img from background_image
    for div in div_list:
        style_text = div.attrs['style']
        id_img = style_text.split('/')[-1].split('_')[0]
        link_img = 'https://www.flickr.com/photos/'+link_text[4]+'/'+id_img+'/sizes/h/'
        print(link_img)
        download_img(link_img, id_img, direct)


# Download img
def download_img(link_img, id_img, direct):
    # link_img = "https://www.flickr.com/photos/trongveostudio/49433490728/sizes/h/"
    source = urllib.request.urlopen(link_img)
    soup = BeautifulSoup(source)
    div_list = soup.find_all('img')
    # print(div_list[2].attrs['src'])
    link_direct = direct+'/'+str(id_img)+'.jpg'
    with open(link_direct, mode='wb') as f:
        respons = requests.get(div_list[2].attrs['src'])
        f.write(respons.content)


for i in album_div:
    # print(i.a.attrs['title'], i.a.attrs['href'])
    print(i.attrs['href'])
    get_id_img(i.attrs['href'], auth_dir)

