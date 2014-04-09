'''
Created on 09-Apr-2014

@author: devanshu
'''
import smtplib
import urllib2


class MinPriceFinder(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.user = 'email_id'
        self.pwd = 'password'
        self.smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        

    def send_email_of_price_list(self, url, receiver):
        '''
        '''
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        page_html = the_page.splitlines()
        self.smtpserver.ehlo()
        self.smtpserver.starttls()
        self.smtpserver.ehlo
        self.smtpserver.login(self.user, self.pwd)
        header = 'To:' + receiver + '\n' + 'From: ' + self.user + '\n' + 'Subject:testing \n' 
        min_price = self.get_min_price_for_day(page_html)
        airline_name = self.get_airline_name_for_min_price(page_html, min_price)
        return airline_name, min_price
                
    def get_min_price_for_day(self, a):
        '''
        '''
        for b in a:
            if 'lowestPriceDisplayed' in b:
                start_index = b.index("'") + 1
                finish_index = b.index(".0'")
                min_price = int(b[start_index:finish_index])
                return min_price


    def get_airline_name_for_min_price(self, a, min_price):
        '''
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
