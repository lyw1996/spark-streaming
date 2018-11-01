# coding: utf-8
import re
from lxml import etree
import requests
import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.mfw
collection = db.mafengwo



def start_requests(self):
    # 列表页请求头
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               'Cache-Control': 'no-cache',
               'Connection': 'keep-alive',
               'Cookie': 'mfw_uuid=5bd163d3-f1eb-63af-fa5b-61dccbfb7936; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-10-25+14%3A33%3A55%22%3B%7D; uva=s%3A78%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1540449236%3Bs%3A10%3A%22last_refer%22%3Bs%3A6%3A%22direct%22%3Bs%3A5%3A%22rhost%22%3Bs%3A0%3A%22%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1540449236%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5bd163d3-f1eb-63af-fa5b-61dccbfb7936; UM_distinctid=166a9ee11198c4-0a5bde04af9e8a-346c780e-13c680-166a9ee111bf63; __mfwlv=1540690537; __mfwvn=9; all_ad=1; PHPSESSID=88hdrc68ks61l3rlkdpmobsdf5; CNZZDATA30065558=cnzz_eid%3D250181906-1540446445-%26ntime%3D1540689452; __mfwlt=1540693400',
               'Host': 'www.mafengwo.cn',
               'Pragma': 'no-cache',
               'Referer': 'http://www.mafengwo.cn/search/s.php?q=%E4%B8%8A%E6%B5%B7&p=3&t=info&kt=1',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
               }
    #
    # 请求的是马蜂窝的搜索url
    country = ['青海','日本','瑞士','英国','泰国']
    for k in country:
        # 页面是展示50页内容，所以遍历的50次
        for i in range(51):
            # 拼接url，发送请求，获取响应内容
            url = 'http://www.mafengwo.cn/search/s.php?q='+k+'&p='+str(i)+'&t=info&kt=1'
            res = requests.get(url=url,headers=headers).text
            # str类型转成html类型，便于标签取值
            response = etree.HTML(res)
            # 取列表页url
            urls = response.xpath("//*[@id='_j_search_result_left']/div[1]/div/ul/li/div/div[2]/h3/a/@href")
            # 评论数
            comment = response.xpath("//*[@id='_j_search_result_left']/div[1]/div/ul/li/div/div[2]/ul/li[2]/text()")
            # 取到如果有评论数就去正则去出数字,没有的给一个None  比如：评论（121）-------->>>>>121
            if comment:
                comment = re.sub(r'\n| ', '', comment)
                comment = re.findall(r'\d+', comment)
            else:
                comment = None
            # 取到如果有收藏数就去正则去出数字,没有的给一个None  比如：收藏（6758）-------->>>>>6759
            browse = response.xpath("//*[@id='_j_search_result_left']/div[1]/div/ul/li[15]/div/div[2]/ul/li[3]/text()")
            if browse:
                browse = re.sub(r'\n| ', '', browse)
                browse = re.findall(r'\d+', browse)

                info = {'urls':urls, 'comment':comment, 'browse':browse}
                parse_details(info,k)

def parse_details(info,k):
    # 详情页请求头
     headers1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'zh-CN,zh;q=0.9',
                 'Cache-Control': 'max-age=0',
                 'Connection': 'keep-alive',
                 'Cookie': 'mfw_uuid=5bd163d3-f1eb-63af-fa5b-61dccbfb7936; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-10-25+14%3A33%3A55%22%3B%7D; uva=s%3A78%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1540449236%3Bs%3A10%3A%22last_refer%22%3Bs%3A6%3A%22direct%22%3Bs%3A5%3A%22rhost%22%3Bs%3A0%3A%22%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1540449236%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5bd163d3-f1eb-63af-fa5b-61dccbfb7936; UM_distinctid=166a9ee11198c4-0a5bde04af9e8a-346c780e-13c680-166a9ee111bf63; PHPSESSID=jgc53ahh96086n0o78dt1acom7; __mfwlv=1540556643; __mfwvn=2; __mfwlt=1540558446',
                 'Host': 'www.mafengwo.cn',
                 'Referer': 'http://www.mafengwo.cn/',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', }
     urls = info['urls']
     for url in urls:
        res = requests.get(url,headers=headers1).text
        response = etree.HTML(res)
        title = response.xpath("//*[@id='_j_cover_box']/div[3]/div[2]/div/h1/text()")
        # 标题
        if title:
            title = title[0]
        else:
            title = None
        # 文章正文
        note = response.xpath('//p[@class="_j_note_content _j_seqitem"]/text()')
        note = re.sub(r'\n| |\xa0', '', ''.join(note))
        # 时间
        time = response.xpath('//li[@class="time"]/text()')
        if time:
            time = time[-1]
        else:
            time = None
        # 人物
        people = response.xpath('//li[@class="people"]/text()')
        if people:
            people = people[-1]
        else:
            people = None
        # 花销
        cost = response.xpath('//li[@class="cost"]/text()')
        if cost:
            cost = cost[-1]
        else:
            cost = None
        # 天数
        day = response.xpath('//li[@class="day"]/text()')
        if day:
            day = day[-1]
        else:
            day = None
        # 国家
        country = k
        data = {'title':title,
                'time':time,
                'people':people,
                'cost':cost,
                'day':day,
                'country':country,}
        # 详情页的信息收藏数，和评论数加到data
        data.update(info)
        # 插入mongodb
        collection.inter(data)

if __name__ == '__main__':
    start_requests()