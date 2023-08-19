from selenium import webdriver


def get_options(headers,ip_proxy=None):
    options = webdriver.chrome.options.Options()
    for (key,value) in headers.items():
        options.add_argument('%s="%s"' % (key, value))
    options.add_argument('headless')
    if ip_proxy is not None:
        options.add_argument(ip_proxy)
    return(options)


def get_driver(headers, ip_proxy=None):
    option = get_options(headers, ip_proxy)
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.amazon.com')
    cookies=driver.get_cookies()
    driver.quit()
    ck = dict()
    for i in cookies:
        ck[i['name']] = i['value']

    headers.update({"Cookie":' ;'.join([k+'='+v for (k,v) in ck.items()])})
    option = get_options(headers, ip_proxy)
    driver = webdriver.Chrome(options=option)


    return(driver)