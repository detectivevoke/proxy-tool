import time
import json
import random
import requests
import os
import threading
class Proxy:
    def __init__(self):
        self.urls = ['http://alexa.lr2b.com/proxylist.txt', 'https://proxyspace.pro/https.txt', 'https://proxyspace.pro/http.txt', 'http://rootjazz.com/proxies/proxies.txt', 'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt', 'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt', 'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt', 'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt', 'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt', 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt', 'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt', 'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt', 'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt', 'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt', 'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/http.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/https.txt', 'https://rootjazz.com/proxies/proxies.txt', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt']
        self.config = json.loads(open("config.json","r").read())
        self.threads = int(self.config["threads"])
        self.timeout = int(self.config["timeout"])
        self.test_url = self.config["test_url"]
        self.sc = self.config["scrape"]
        self.alive = 0
        self.dead = 0
        self.check = []
        self.scraped = []
        self.c = 0


    def check_proxies(self):
        while len(self.check) > 0:
            proxy = self.check[0]
            self.check.pop(0)
            try:
                r= requests.get(self.test_url, proxies={"https": "http://{}".format(proxy)},timeout=int(self.timeout))
            except:self.dead = self.dead + 1
            else:
                print("Proxy Working ({}) - Time Taken: {}".format(proxy, r.elapsed))
                self.alive = self.alive + 1
                with open("checked.txt","a") as w:
                    w.write(proxy+"\n")

    def scrape(self):
        for x in self.urls:
            r = requests.get(x)
            y = 0
            for p in r.text.split('\n'):
                if p in self.scraped:
                    pass
                else:
                    self.scraped.append(p)
                    self.c +=1
                    y +=1
        print("{} Scraped!".format(y))
        with open("proxies.txt","a+") as f:
            f.truncate(0)
            for p in self.scraped:
                p = p.strip("\n")
                f.write("{}\n".format(p))
        
    def checker(self):
        try:
            os.system("cls")
        except:
            pass
        
        self.file_name = self.config["file_name"]

        if not self.file_name:
            print("{} is not a file!".format(self.file_name))
            return ""
        else:
            pass
        
        self.proxy_type = self.config["proxy_type"]

        os.system("cls")

        with open(self.file_name, "r") as f:
            self.count = sum(1 for proxy in f)
            print("Loaded {} proxies!".format(self.count))
        with open(self.file_name, "r+") as f:
            lines = f
            for proxy in lines:
                self.check.append(proxy.strip("\n"))
        threads = []
        
        for i in range(self.threads):
            threads.append(threading.Thread(target=self.check_proxies))
            threads[i].setDaemon(True)
            threads[i].start()

        self.checking = True

        while self.checking:
            if len(threading.enumerate())-1==0:
                self.checking = False
            else:
                os.system("title "+f"""Detective Voke#9732 - Working: {self.alive} - Not Working: {self.dead}""")

    def main(self):
        if self.sc:
            print("Scraping started!")
            self.scrape()
            pass
        else:
            print("Scraping is not enabled, skipping...")
            pass

        self.checker()

Proxy().main()