from amazon_crawl.process.process_category_page import get_category_info
from amazon_crawl.core.source_page import read_data_from, get_soup
import pandas as pd


def serch_category_tree(start_url, web_driver):
    driver = read_data_from(web_driver, start_url)
    res = get_soup(driver)
    while res.find('div',attrs={'role':"group"}) is None:
        print(1)
        res = get_soup(driver)

    urls = get_category_info(res)

    urls = pd.DataFrame({'channel':urls[0],'url':urls[1],'parent':urls[2]})

    data = pd.DataFrame()
    data = pd.concat([urls, data])
    crawl_data = data
    cnt = 1
    while crawl_data[~crawl_data.channel.isin(['root'])].shape[0] > 0 and cnt <= 20:
        print('level', cnt)
        level_data = pd.DataFrame({'channel':[],'url':[],'parent':[]})
        print(crawl_data[~crawl_data.channel.isin(['root'])].groupby('parent').count())

        for name, group in crawl_data[~crawl_data.channel.isin(['root'])].groupby('parent'):
            print('rootL:', name, group.shape[0])
            crawl_data =  pd.DataFrame({'channel':[],'url':[],'parent':[]})
            group_data = pd.DataFrame({'channel':[],'url':[],'parent':[]})

            for index, row in group.iterrows():
                print('root:', name, row[0])
                driver = read_data_from(web_driver, 'https://www.amazon.com' + row[1], k=0)
                res = get_soup(driver)

                while res.find('div',attrs={'role':"group"}) is None:
                    print(2)
                    driver = read_data_from(web_driver, 'https://www.amazon.com' + row[1], k=0)
                    res = get_soup(driver)

                res = get_category_info(res)

                res = pd.DataFrame({'channel':res[0],'url':res[1], 'parent':res[2]})

                if None in res.url.tolist():
                    res = res[res.url.isnull()]
                    temp = pd.DataFrame({'parent':res.channel.tolist()})
                    temp = temp.assign(channel='root',
                                       url = 'www.amazon.com')
                    group_data = pd.concat([temp, group_data])
                    print('end batch')
                    #break
                    ##最后一级
                else:
                    group_data = pd.concat([res, group_data])
                    crawl_data = pd.concat([res, crawl_data])
                    group_data = group_data.drop_duplicates()
                    crawl_data = crawl_data.drop_duplicates()
            level_data = pd.concat([group_data, level_data])

        data = pd.concat([level_data, data])
        data = data.drop_duplicates()
        cnt += 1

    return(data)