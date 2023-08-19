from bs4 import BeautifulSoup
import time
from .base_func import scroll


def get_soup(driver):

    soup = BeautifulSoup(driver.page_source, "html.parser").body
    k = 1

    while soup is None or soup.text == 'Request was throttled. Please wait a moment and refresh the page':
        print('get soup {} times.'.format(k))
        k += 1
        driver.refresh()
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser").body

    return(soup)


def read_data_from(driver, url, postal=None, k=15):
    print('read data from:',url)

    if url is not None:

        driver.get(url)

        if postal is not None:
            posta = get_address(driver)
            while posta != postal:
                print(posta)
                change_address(driver, postal)
                posta = get_address(driver)
        if k > 0:
            scroll(driver)
            time.sleep(k)
    return(driver)


def get_address(driver):

    try:
        print('get address')
        soup = get_soup(driver)
        print(soup.find(id='glow-ingress-line2').text)
        posta = soup.find(id='glow-ingress-line2').text.split()[-1].replace('\u200c','')
        print('get address success')
        return(posta)
    except:
        print('get address fail')
        return(None)


def change_address(driver, postal):

    driver.get('https://www.amazon.com')
    try:
        posta = get_address(driver)
    except:
        posta = None

    k = 1
    while posta != postal:
        while True:
            print('change address {} times'.format(k))
            k += 1

            while find_element(driver, "GLUXChangePostalCodeLink") == None:
                try:
                    print('setp One')
                    driver.find_element_by_xpath('//span[contains(text(), "Deliver to")]').click()
                    # driver.find_element_by_id('nav-global-location-slot').click()
                    time.sleep(3)
                except Exception as e:
                    print('setp One fail')
                    driver.refresh()
                    time.sleep(5)
                    continue

            try:
                print('setp Two')
                driver.find_element_by_id("GLUXChangePostalCodeLink").click()
                time.sleep(2)
            except:
                pass

            try:
                print('setp Three')
                driver.find_element_by_id('GLUXZipUpdateInput').send_keys(postal)
                time.sleep(1)
                break
            except Exception as NoSuchElementException:
                try:
                    driver.find_element_by_id('GLUXZipUpdateInput_0').send_keys(postal.split('-')[0])
                    time.sleep(1)
                    driver.find_element_by_id('GLUXZipUpdateInput_1').send_keys(postal.split('-')[1])
                    time.sleep(1)
                    break
                except Exception as NoSuchElementException:
                    driver.refresh()
                    time.sleep(10)
                    continue
            print("重新选择地址")
        driver.find_element_by_id('GLUXZipUpdate').click()
        #driver.find_element_by_id('GLUXConfirmClose').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        posta = get_address(driver)

    print('set posta success',posta)