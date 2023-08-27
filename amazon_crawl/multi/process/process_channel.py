from amazon_crawl.multi.util.webdriver import init_driver
from amazon_crawl.pages import get_product_info_channel, reshape_channel_page
from amazon_crawl.util.base_utils import retry


def process_channel(z):
    max_try = 5
    try_times = 0
    if try_times <= max_try:
        try:
            driver = init_driver()
            ttt = get_product_info_channel('https://www.amazon.com' + z[0], driver)
            ttt = ttt.assign(channel = z[1],
                             parent = z[2])
            return(ttt)
        except:
            try_times += 1
            print("try {} time".format(try_times))
    else:
        return(None)
