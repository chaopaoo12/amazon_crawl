from amazon_crawl.multi.util.webdriver import init_driver
from amazon_crawl.pages import get_product_info_channel

def process_channel(z):
    driver = init_driver()
    ttt = get_product_info_channel('https://www.amazon.com' + z[0], driver)
    ttt = ttt.assign(channel = z[1],
                     parent = z[2])
    return(ttt)