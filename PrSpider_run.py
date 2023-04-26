from PrSpider import PrSpiders


class Spider(PrSpiders):

    def __init__(self, url, encode='utf-8', verify=False,
                 retry=None, method=None, header=None, log='info', stdout=None,
                 timeout=None, download_num=None, download_delay=None, task=None

                 ):
        self.url = url
        self.encode = encode
        self.verify = verify
        self.retry = retry
        self.method = method
        self.header = header
        self.log_stdout = stdout
        self.log_level = log

        super().__init__()

    def start_requests(self, **kwargs):
        # PrSpiders.Requests(url=self.url, callback=self.parse, encoding=self.encode,
        #                    verify=self.verify, retry_time=self.retry, method=self.method, headers=self.header
        #                    )
        pass

    def parse(self, response):
        print(response.text)
        # print(response.code, response.url)
