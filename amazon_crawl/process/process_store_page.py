import pandas as pd

def get_info_bystore(html):
    docs = html.find(attrs={'data-component-type':'s-search-results'}).find_all(attrs={'data-component-type':'s-search-result'})

    pages_h = html.find(attrs={'role':'navigation'})
    if pages_h is not None:
        pages = pages_h.find(text='Next')
        if pages is None:
            pages = pages_h.find(text='Next page')
    else:
        pages = None

    if pages is not None:
        pages = 'https://www.amazon.com' + pages.get('href')

    return([doc.find(class_='s-title-instructions-style').find(class_='puis-label-popover-default').find('span').text if doc.find(class_='s-title-instructions-style').find(class_='puis-label-popover-default') is not None else None for doc in docs],
           [doc.find(class_='s-title-instructions-style').find('h2').find('span').text for doc in docs],
           [doc.find(attrs={'data-component-type':'s-product-image'}).find('a').get('href') for doc in docs],
           [doc.get('data-asin') for doc in docs],
           [doc.find(class_='a-icon-alt').text.replace(' out of 5 stars','') if doc.find(class_='a-icon-alt') is not None else None for doc in docs],
           [doc.find(class_='a-size-base s-underline-text').text if doc.find(class_='a-size-base s-underline-text') is not None else None for doc in docs],
           [doc.find(class_='a-price').find(class_='a-offscreen').text.replace('$','').replace('\xa0','') if doc.find(class_='a-price') is not None else 0 for doc in docs],
           [doc.find(class_='a-price-symbol').text if doc.find(class_='a-price-symbol') is not None else None for doc in docs],
           [doc.find(class_='a-size-extra-large s-color-discount puis-light-weight-text').text if doc.find(class_='a-size-extra-large s-color-discount puis-light-weight-text') is not None else None for doc in docs],
           [doc.find(class_='a-price a-text-price').find(class_='a-offscreen').text if doc.find(class_='a-price a-text-price') is not None else None for doc in docs],
           [doc.find(attrs={'data-component-type':'s-coupon-component'}).find(class_='a-color-base').text if doc.find(attrs={'data-component-type':'s-coupon-component'}) is not None else None for doc in docs],
           [doc.find(attrs={'aria-label':'Amazon Prime'}).get('aria-label') if doc.find(attrs={'aria-label':'Amazon Prime'}) is not None else None for doc in docs],
           [doc.find(attrs={'aria-label':'FREE Shipping by Amazon'}).text if doc.find(attrs={'aria-label':'FREE Shipping by Amazon'}) is not None else None for doc in docs],
           pages
           )


def read_info_bystore(html):
    Sponsored, title, href, asin, star, comments, price, symbol, discount,off_price,coupon,prime,shipping,pages  = get_info_bystore(html)
    temp = pd.DataFrame({'Sponsored': Sponsored,
                         'title':title,
                         'href': href,
                         'asin': asin,
                         'star': star,
                         'comments': comments,
                         'price': price,
                         'symbol': symbol,
                         'discount': discount,
                         'off_price': off_price,
                         'coupon': coupon,
                         'prime':prime,
                         'shipping':shipping})
    return(temp)


