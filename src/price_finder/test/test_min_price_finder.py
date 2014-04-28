'''
Created on 09-Apr-2014

@author: devanshu
'''
from src.price_finder.min_price_finder import MinPriceFinder


def test_min_price():
    min_price_finder = MinPriceFinder()
    min_price_finder.get_price_between_two_dates('DEL', 'LKO', '22/05/2014', '01/08/2014')
#    min_price_finder.get_price_between_two_dates('LKO', 'DEL', '22/05/2014', '01/08/2014')
    

if __name__ == '__main__':
    test_min_price()
