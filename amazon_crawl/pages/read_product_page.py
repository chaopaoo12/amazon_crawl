from amazon_crawl.core.source_page import read_data_from, get_soup
from amazon_crawl.process.process_product_info import get_fivepoints, get_labels

def get_product_info(driver, url):
    driver = read_data_from(driver, url)
    res = get_soup(driver)
    five_points = get_fivepoints(res)
    res_d = get_labels(res)
    res_d['five_points'] = five_points
    return(res_d)