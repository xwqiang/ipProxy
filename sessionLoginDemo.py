import requests
HEADER = {'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          }
login_url='http://bytest.cards.kuyun.com/cards/login'
url='http://bytest.cards.kuyun.com/cards/getBonusInfoAjax'
s = requests.Session()  # 可以在多次访问中保留cookie
s.post(login_url, {'username':'xuwuqiang', 'password': '1',}, headers=HEADER)  # POST帐号和密码，设置headers
r = s.post(url)
print(r.content)