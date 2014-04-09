'''
Created on 09-Apr-2014

@author: devanshu
'''
from src.price_finder.min_price_finder import MinPriceFinder


def test_min_price():
#    mmt_url_1 = "http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/LKO_DEL_17-05-2014"
    min_price_finder = MinPriceFinder()
    airline_name, min_price = min_price_finder.make_mmt_url('LKO', 'DEL', '17', '05', '2014')
    print airline_name, " ", min_price

if __name__ == '__main__':
    test_min_price()
