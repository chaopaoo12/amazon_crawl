from amazon_crawl.core.source_page import read_data_from, get_soup
from amazon_crawl.core.base_func import scroll
from amazon_crawl.process.process_channel_page import read_info_byChannel
import time


def reshape_channel_page(url):
    pages = ['','&pg=2','&pg=3','&pg=4','&pg=5','&pg=6','&pg=7','&pg=8']
    pages = ['/'.join(url.split('/')[:-1]) + '/ref=zg_bs_pg_2_' + url.split('/')[-3] + '?_encoding=UTF8' + i for i in pages]
    return(pages)

def get_product_info_channel(url, driver):

    driver = read_data_from(driver, url, k = 15)
    html = get_soup(driver)
    temp = read_info_byChannel(html)
    next_page = html.find('li',attrs={'class':"a-last"})
    if next_page is not None:
        temp_k = 0
        try_k = 0
        while temp.shape[0] < 45:
            try_k += 1
            print(temp.shape)
            if temp.shape[0] == 0 or temp_k == temp.shape[0]:
                driver = read_data_from(driver, url, k = 15)
            try:
                scroll(driver)
                time.sleep(6)
            except:
                print('Scroll FAIL 2')
                pass
            time.sleep(5)
            html = get_soup(driver)
            temp = read_info_byChannel(html)
            temp_k = temp.shape[0]
            if try_k > 5:
                break
    driver.quit()
    return(temp)

