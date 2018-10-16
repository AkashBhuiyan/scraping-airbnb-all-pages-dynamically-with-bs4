# div class =_fhph4u

    #_div class = _gig1e7

        # titel -> div class = _jnrahhr
        # price -> span class = _17oldnte
        # no_of_review_users -> span class = _q27mtmr



from selenium import webdriver
from bs4 import BeautifulSoup
import imp

import sys
imp.reload(sys)


class AirBnbDetail:

    def __init__(self):
        self.title = ''
        self.price = ''
        self.number_of_user_review = ''

class CollectAirBnbInfo:

    def __init__(self):
        self.driver = ""
        self.page_seq = 0
        self.no_of_page = 0

    def collect_given_link_data(self, url, air_bnb_details_list):

        self.driver = webdriver.PhantomJS(
            executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

        self.driver.get(url)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        div1 = soup.find('div', class_='_fhph4u')

        #print(div1)

        for div2 in div1.find_all('div', class_='_gig1e7'):

            air_bnb_obj = AirBnbDetail()
            #print(div2)
            title_div = div2.find('div', class_='_jnrahhr')
            air_bnb_obj.title = title_div.text
            #print(title_div.text)
            price_span = div2.find('span', class_='_17oldnte')
            air_bnb_obj.price = price_span.text
            #print(price_span.text)
            no_of_review_user = ''
            if div2.find('span', class_='_q27mtmr') !=None:
                no_of_review_user = div2.find('span', class_='_q27mtmr')
                air_bnb_obj.number_of_user_review = no_of_review_user.findNextSibling().text
                #print(no_of_review_user.findNextSibling().text)

            #print('\n')

            air_bnb_details_list.append(air_bnb_obj)


    def collect_no_of_page(self, url):

        self.driver = webdriver.PhantomJS(
            executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

        self.driver.get(url)
        #div class = '_1bdke5s'
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        div = soup.find_all('div', class_='_1bdke5s')
        #print(div[1].text)

        return div[1].text # return last index's text



    def collec_all_page_data(self, url, air_bnb_details_list):

        if len(air_bnb_details_list)==0:
            self.collect_given_link_data(url=url, air_bnb_details_list= air_bnb_details_list)

        else:
            each_page_item = 18
            total_item = each_page_item * self.no_of_page

            self.page_seq += each_page_item
            if self.page_seq <= total_item:
                page = '&items_offset=' + str(self.page_seq)

                self.collect_given_link_data(url=url + page, air_bnb_details_list=air_bnb_details_list)



if __name__ == '__main__':
    url = 'https://www.airbnb.com/s/Bangladesh/homes?checkin=2018-10-20&checkout=2018-10-24&adults=1&children=0&infants=0&click_referer=t%3ASEE_ALL%7Csid%3Adf2321a3-0673-4b0a-b399-a28875aca804%7Cst%3ALANDING_PAGE_MARQUEE&title_type=NONE&refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=DN1j4-rh'

    air_bnb_all_info_obj = CollectAirBnbInfo()
    air_bnb_details_list = []
    no_of_page = int(air_bnb_all_info_obj.collect_no_of_page(url))
    print(no_of_page)
    air_bnb_all_info_obj.no_of_page = no_of_page
    if no_of_page ==1 or no_of_page== None:
        air_bnb_all_info_obj.collec_all_page_data(url, air_bnb_details_list)

    else:
        for page_no in range(1, no_of_page):
            air_bnb_all_info_obj.collec_all_page_data(url, air_bnb_details_list)


    for air_bnb_details in air_bnb_details_list:
        print(air_bnb_details.title)
        print(air_bnb_details.price)
        print(air_bnb_details.number_of_user_review, '\n')

    print(len(air_bnb_details_list))
    air_bnb_all_info_obj.driver.quit()

