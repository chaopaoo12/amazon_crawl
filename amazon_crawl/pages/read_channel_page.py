from amazon_crawl.core.source_page import read_data_from, get_soup
from amazon_crawl.core.base_func import scroll
from amazon_crawl.process.process_channel_page import read_info_byChannel
import pandas as pd
import time


def get_product_info_channel(url, driver):
    pages = ['','&pg=2','&pg=3','&pg=4','&pg=5','&pg=6','&pg=7','&pg=8']
    pages = [url + i for i in pages]
    res = pd.DataFrame()
    for i in pages:
        driver = read_data_from(driver, i, k = 15)
        html = get_soup(driver)
        temp = read_info_byChannel(html)
        while temp.shape[0] < 50:
            print(temp.shape)
            if temp.shape[0] == 0:
                driver = read_data_from(driver, i, k = 15)
            scroll(driver)
            time.sleep(5)
            html = get_soup(driver)
            temp = read_info_byChannel(html)
        res = res.append(temp)

    return(res)