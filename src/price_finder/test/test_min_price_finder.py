'''
Created on 09-Apr-2014

@author: devanshu
'''
from src.price_finder.min_price_finder import MinPriceFinder


def test_min_price():
    mmt_url_1 = "http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/LKO_DEL_17-05-2014"
    mmt_url_2 = "http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/BOM_CCU_26-06-2014"
    mmt_url_3 = "http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/AMD_MAA_06-04-2014"
    receiver = 'dwivedi.devanshu@gmail.com'
    min_price_finder = MinPriceFinder()
    airline_name, min_price = min_price_finder.send_email_of_price_list(mmt_url_3, receiver)
    print airline_name, " ", min_price


if __name__ == '__main__':
    test_min_price()
