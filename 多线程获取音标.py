import urllib.request
from multiprocessing import Pool
import re
import requests
import urllib.request as req
from urllib.parse import unquote


def search(e,url):
    r = req.Request(url + e)
    s = req.urlopen(r)
    page = s.read().decode('utf-8')
    # print(page)
    try:
        v = re.search('>美\s+<span class="phonetic">([\S\W\]]+?)<', page)
        # print(e + "\t" + v.group(1))
        return v.group(1)

    except(AttributeError):
        print("检查单词拼写" + e)


if __name__ == '__main__':
    url = 'http://dict.youdao.com/w/eng/'
    tone = []

    with open('./a.txt', 'r') as a:
        item = a.read().split('\n')
    p = Pool(20)
    for i in item:
        res = p.apply_async(search, args=(i,url))
        tone.append(res)
    p.close()
    p.join()

    # for i in tone:
    #     print(str(i.get()))
    with open('./b.txt','a+',encoding='utf-8') as b:
        for i in tone:
            b.write(str(i.get())+"\n")