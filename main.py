import googlesearch
import urllib.request, urllib.error, urllib.parse
import sys
from bs4 import BeautifulSoup
import re


blok = 70
blok = sys.argv[1]
search = googlesearch.search('prodaja stanova blok ' + blok, num_results = 5)


stanovi = []

lSearch = list(search)
print(lSearch)
url = lSearch[0]
page = 1
while True:
    urlSearch = url + '?page=' + (str)(page)
    page = page + 1
    response = urllib.request.urlopen(urlSearch)
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent, "html.parser")
    mydivs = soup.find_all("div", {"class": "col-md-12 col-sm-12 col-xs-12 col-lg-12"})
    if (len(mydivs) < 1):
        break

    for divs in mydivs:#data-value="145.000"><i>
        stan = []
        tt = re.search('data-value="(.{0,8})"><',divs.__str__())
        if (tt):
            stan.append(tt.group(1))
        tt = re.search('price-by-surface"><span>(.*)€\/m',divs.__str__())
        if (tt):
            stan.append(tt.group(1))
        #<li class="col-p-1-3"><div class="value-wrapper">107&nbsp;m<sup>2
        tt = re.search('<div class="value-wrapper">(.{0,10})<sup>2</sup><span class="legend">Kvadratura</span></div>',divs.__str__())
        if (tt):
            stan.append(tt.group(1))#
            #

        tt = re.search('<div class="value-wrapper">(.{0,10})<span class="legend">Broj soba</span></div>',divs.__str__())
        if (tt):
            stan.append(tt.group(1))

        tt = re.search('<div class="value-wrapper">(.{0,10})<span class="legend">Spratnost</span></div>',divs.__str__())
        if (tt):
            stan.append(tt.group(1))

        tt = re.search('<h3 class="product-title"><a href="(.*)">(.*)</a></h3>',divs.__str__())
        if (tt):
            stan.append(tt.group(2))
            stan.append(tt.group(1))
        stanovi.append(stan)
prosek = 0
for stan in stanovi:
    print("\n##############################\n")
    print ("STAN : " + stan[5])
    if len(stan) > 6:
        print("LINK : " + stan[6])
    print("CENA : " + stan[0])
    print("CENA KVADRATA : " + stan[1])
    prosek = prosek + int(stan[1].replace(".",""))
    print("KVADRATURA : " + stan[2])
    print("BROJ SOBA : " + stan[3])
    print("SPRATNOST : " + stan[4])
    print("\n##############################\n")


print("PROSECNA CENA STANA : ")
print(prosek/len(stanovi))



