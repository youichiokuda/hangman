import urllib.request as request
from bs4 import BeautifulSoup
import datetime
import time
def job():
    #str_timestamp = now.strftime("%y/%m/%d_%H:%M:%S")
    now = datetime.datetime.now()
    print('今の時間は')
    print(now.strftime("%y/%m/%d_%H:%M:%S"))

job()

def get_stock_price(url):
    response = request.urlopen(url)
    bs = BeautifulSoup(response, 'html.parser')
    stoksPrice = bs.select('.stoksPrice')[1].text
    return stoksPrice


url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
result = get_stock_price(url)
print(f'日経平均株価は{result}円です。')

url2 = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8411.T'
result = get_stock_price(url2)
print(f'みずほ銀行の株価は`{result}円です。')