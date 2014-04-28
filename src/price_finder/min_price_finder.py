'''
Created on 09-Apr-2014

@author: devanshu
'''
import datetime
import urllib2


class MinPriceFinder():

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def get_price_between_two_dates(self, src_city, dest_city, start_date_str, end_date_str):
        '''
        src_city: the source city from where you plan to travel from
        dest_city: the destination city where you plan to travel to
        start_date_str, end_date_str: the tentative start and end date in (dd/mm/yyyy)
                                         format between which you plan to travel
        '''
        start_date_param = start_date_str.split('/')
        end_date_param = end_date_str.split('/')
        start_date = datetime.date(int(start_date_param[2]), int(start_date_param[1]), int(start_date_param[0]))
        end_date = datetime.date(int(end_date_param[2]), int(end_date_param[1]), int(end_date_param[0]) + 1)
        for single_date, day in self.daterange(start_date, end_date):
            airline_name, min_price = self.make_mmt_url(src_city, dest_city, single_date.day, single_date.month, single_date.year)
            print single_date, " ", day, " ", airline_name, " ", min_price
    
    def make_mmt_url(self, src_city, dest_city, dd, mm, yyyy):
        '''
        Function takes input of your source and destination city and date parameters to form the url
        Returns the airline name and min price 
        '''
        base_url = "http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/{0}_{1}_{2}-{3}-{4}"
        mmt_url = base_url.format(src_city, dest_city, dd, mm, yyyy)
        return self.get_min_price_for_the_day(mmt_url)

    def get_min_price_for_the_day(self, url):
        '''
        The function takes input of the dynamically formed url and returns the airline name 
        and minimum price of the day.
        '''
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        page_html = response.read()
        page_html_list = page_html.splitlines()
        min_price = self.get_price(page_html_list)
        airline_name = self.get_airline_name_for_min_price(page_html_list, min_price)
        return airline_name, min_price
                
    def get_price(self, a):
        '''
        The function iterates through the list of line of source html to get the minimum price.
        '''
        for b in a:
            if 'minfare' in b:
                start_index = b.index("= ") + 1
                finish_index = b.index(".0")
                min_price = int(b[start_index:finish_index])
                return min_price


    def get_airline_name_for_min_price(self, a, min_price):
        '''
        The function iterates through the list of line of source html to get the 
        airline name corresponding to minimum price.
        '''
        for index, c in enumerate(a):
            if min_price and ('flL mtop5 mleft3 vallabel' in c):
                flight_name_start_index = c.index('vallabel">') + 10
                flight_name_end_index = c.index('</label>')
                flight_name = c[flight_name_start_index : flight_name_end_index]
                next_row = a[index + 1]
                price_start_index = next_row.index('Rs. ') + 4
                airline_price = int(next_row[price_start_index:].replace(',', ''))
                if (min_price == airline_price):
                    return flight_name
    
    def daterange(self, start_date, end_date):
        '''
        The function is a generator and iterates between the start and end date
        '''
        for n in xrange(int ((end_date - start_date).days)):
            return_date = start_date + datetime.timedelta(n)
            yield return_date, return_date.strftime('%A')

