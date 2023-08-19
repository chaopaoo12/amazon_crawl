from process.process_store_page import read_info_bystore
import time
from core.source_page import read_data_from, get_soup
from core.base_func import scroll
import pandas as pd


def get_product_byasin(asin, driver):
    base_url = 'https://www.amazon.com/s?k='
    products = pd.DataFrame()
    for a in asin:
        search_url = base_url + a
        driver = read_data_from(driver, search_url)
        html = get_soup(driver)
        temp = read_info_bystore(html)
        while temp.shape[0] < 50:
            scroll(driver)
            time.sleep(5)
            html = get_soup(driver)
            temp = read_info_bystore(html)
        products = products.append(temp)
    return(products)


def get_product_info_store(driver, store, market_id):

    base_url = 'https://www.amazon.com/s?me={store}&marketplaceID={market_id}'.format(store=store, market_id=market_id)
    pages = base_url
    res = pd.DataFrame()
    while pages is not None:
        driver = read_data_from(driver, pages)
        html = get_soup(driver)
        temp = read_info_bystore(html)
        res = res.append(temp)
    res = res.assign(store = store,
                     market_id = market_id)
    return(res)