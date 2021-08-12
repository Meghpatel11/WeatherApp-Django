from django.shortcuts import render

from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
# Create your views here.

def get_html(search):
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    session = HTMLSession()
    link = f"https://www.google.com/search?q=weather+in+{search}"

    html_content = session.get(link,headers=headers).content
    return html_content

def home(request):
    context=None

    if 'city' in request.GET:

        city = request.GET.get('city')
        html_content=get_html(city)

        soup=BeautifulSoup(html_content,"html.parser")

        region = soup.find('div',attrs={'id': 'wob_loc'}).text
        temp = soup.find('span',attrs={'id': 'wob_tm'}).text
        time = soup.find('div',attrs={'id': 'wob_dts'}).text
        stats = soup.find('span',attrs={'id': 'wob_dc'}).text
        
        context = {'region':region,'temp':temp,'time':time,'stats':stats}

    return render(request,'core/home.html',context)
