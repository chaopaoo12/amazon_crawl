from fake_useragent import UserAgent
from amazon_crawl.core import get_driver

def init_driver(proxy = '--proxy-server=http://127.0.0.1:10809'):
    ua = UserAgent()

    ua_use = ua.random
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Cache-Control': 'max-age=0',
               'User-Agent': ua_use,
               'Connection': 'keep-alive',
               }
    driver = get_driver(headers, proxy)
    return(driver)