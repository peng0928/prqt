import json
from PrSpider import PrSpiders
from spider_sqlite import *


class Spider(PrSpiders):

    def __init__(self, url=None, encode='utf-8', verify=False,
                 retrytime=True, method='get', header={}, loger='info', stdout=False,
                 timeout=3, download_num=5, download_delay=1, worker=5, task=None, data=None
                 ):
        self.url = url
        self.worker = int(worker)
        self.encode = encode
        self.verify = verify
        self.method = method
        self.header = header
        self.log_stdout = stdout
        self.log_level = loger
        self.download_num = int(download_num)
        self.timeout = int(timeout)
        self.download_delay = int(download_delay)
        self.task = task
        self.data = data
        self.retrytime = int(retrytime)
        super().__init__()

    def start_requests(self, **kwargs):
        get_meta = {
            'req_headers': self.header,
            'data': self.data,
        }
        url_list = self.url.split('\n')
        try:
            self.header = eval(self.header)
        except:
            pass
        if self.data:
            if 'json' in str(self.header):
                data = json.loads(self.data)
                data = json.dumps(data)
                PrSpiders.Requests(
                    url=url_list, callback=self.cparse, encoding=self.encode,
                    retry_time=self.retrytime, method=self.method, headers=self.header,
                    timeout=self.timeout, verify=self.verify, meta=get_meta, data=data
                )
            else:
                PrSpiders.Requests(
                    url=url_list, callback=self.cparse, encoding=self.encode,
                    retry_time=self.retrytime, method=self.method, headers=self.header,
                    timeout=self.timeout, verify=self.verify, meta=get_meta, params=self.data
                )
        else:
            PrSpiders.Requests(
                url=url_list, callback=self.cparse, encoding=self.encode,
                retry_time=self.retrytime, method=self.method, headers=self.header,
                timeout=self.timeout, verify=self.verify, meta=get_meta
            )

    def cparse(self, response):
        sql = '''
        insert into "main"."qt_spider" (url, code, req_headers, res_headers, res_len, res_text) VALUES (?, ?, ?, ?, ?, ?)
        '''
        conn.execute(sql, (response.url, response.code, escape_string(str(response.meta)),
                           escape_string(str(response.headers)), response.len, escape_string(response.text)))
        conn.commit()


class Spider_Cookie(PrSpiders):

    def __init__(self, url=None, encode='utf-8', verify=False,
                 retrytime=True, method='get', header={}, loger='info', stdout=False,
                 timeout=3, download_num=5, download_delay=1, worker=5, task=None, data=None
                 ):
        self.url = url
        self.cklist = []
        self.worker = int(worker)
        self.encode = encode
        self.verify = verify
        self.method = method
        self.header = header
        self.log_stdout = stdout
        self.log_level = loger
        self.download_num = int(download_num)
        self.timeout = int(timeout)
        self.download_delay = int(download_delay)
        self.task = task
        self.data = data
        self.retrytime = int(retrytime)
        super().__init__()

    def start_requests(self, **kwargs):

        self.header = eval(self.header)
        url_list = self.url.split('\n')
        cookie = self.header.get('cookie')
        cookie = cookie if cookie else self.header.get('Cookie')
        cookie = cookie.split(';')
        lck = len(cookie)
        for i in range(lck):
            if i == 0:
                s = ';'.join(cookie[1:]).replace(' ', '').replace(';', '; ')
            elif i == lck - 1:
                s = ';'.join(cookie[:-1]).replace(' ', '').replace(';', '; ')
            else:
                s = ';'.join(cookie[:i]).replace(' ', '').replace(';', '; ')
                e = ';'.join(cookie[i + 1:]).replace(' ', '').replace(';', '; ')
                s = s + '; ' + e
            if 'cookie' in self.header:
                self.header.update({'cookie': s})
            if 'Cookie' in self.header:
                self.header.update({'Cookie': s})

            get_meta = {
                'req_headers': self.header,
                'data': self.data,
                's': cookie[i]
            }
            PrSpiders.Requests(
                url=url_list, callback=self.cparse, encoding=self.encode,
                retry_time=self.retrytime, method=self.method, headers=self.header,
                timeout=self.timeout, verify=self.verify, meta=get_meta
            )

    def cparse(self, response):
        code = response.code
        self.responsed = response
        if code != 200:
            s = response.meta.get('s')
            self.cklist.append(s)

    def __del__(self):
        sql = '''
        insert into "main"."qt_spider" (url, code, req_headers, res_headers, res_len, res_text) VALUES (?, ?, ?, ?, ?, ?)
        '''
        text = '\n检测cookie结果\n' + escape_string(str(self.cklist)) + '\n源码\n' + self.responsed.text
        conn.execute(sql, (self.url, self.responsed.code, '检测cookie', '检测cookie', self.responsed.len, text))
        conn.commit()
