import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

browser = webdriver.Firefox()
browser.implicitly_wait(2)
proxy_list=[]
working_prxy=[]

def get_proxies():
    browser.get('http://www.freeproxylists.net/')
    results = browser.find_elements_by_xpath('//table/tbody/tr/td')
    tik = 21
    for x in range(10):
        try:
            proxy_list.append(results[tik].text + ':' + results[tik+1].text)
            tik = tik +10
        except:
            pass
    print(proxy_list)


get_proxies()
