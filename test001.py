#!/user/bin/env python3
# -*- coding: utf-8 -*-
# Time : 2019/6/5 19:03
# Author : "YinTao"
# ============== #

from bs4 import BeautifulSoup
import requests, sys


class Downloader(object):
    def __init__(self):
        self.server = 'https:'
        self.target = 'https://book.qidian.com/info/1014265016#Catalog'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, features='html.parser')
        div = div_bf.find_all('ul', class_='cf')
        a_bf = BeautifulSoup(str(div[0]), features='html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            # print(each.text)
            # print(each.get('href')) # get只寻找直系子标签的关键字   <li><a href='xxx'></li> 如果each是li标签则不能找到href
            self.names.append(each.text)
            self.urls.append(self.server+each.get('href'))


    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding='utf-8'
        html = req.text
        bf = BeautifulSoup(html, features='html.parser')
        texts = bf.find_all('div', class_='read-content j_readContent')[0].text
        texts = texts.replace(texts[1], '\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    downloader = Downloader()
    downloader.get_download_url()
    print('《诸神游戏》开始下载：')
    for i in range(downloader.nums):
        downloader.writer(downloader.names[i], '诸神游戏.txt', downloader.get_contents(downloader.urls[i]))
        print("已下载：%.3f%%"%float(100*i/downloader.nums)+'\r')

        # print("%.3f"%float(i/downloader.nums)+'\r')
    print('下载完成!')
