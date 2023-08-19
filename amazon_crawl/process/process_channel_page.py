import pandas as pd


def get_info_byChannel(html):
    docs = html.find_all(id='gridItemRoot')

    return([doc.find(class_='zg-bdg-text').text for doc in docs],
           [doc.find('div',{'class':['_cDEzb_p13n-sc-css-line-clamp-3_g3dy1',
                                     '_cDEzb_p13n-sc-css-line-clamp-4_2q2cc']}).text if doc.find('div',{'class':['_cDEzb_p13n-sc-css-line-clamp-3_g3dy1','_cDEzb_p13n-sc-css-line-clamp-4_2q2cc']}) is not None else None for doc in docs],
           [doc.find(attrs={'class':'a-link-normal','tabindex':'-1'}).get('href') if doc.find(attrs={'class':'a-link-normal','tabindex':'-1'}) is not None else None for doc in docs],
           [doc.find(class_='p13n-sc-uncoverable-faceout').get('id') if doc.find(class_='p13n-sc-uncoverable-faceout') is not None else None for doc in docs],
           [doc.find(class_='a-icon-alt').text.replace(' out of 5 stars','') if doc.find(class_='a-icon-alt') is not None else None for doc in docs],
           [doc.find(class_='a-size-small').text.replace(',','') if doc.find(class_='a-size-small') is not None else 0 for doc in docs],
           [doc.find(class_='a-size-base').text.replace('$','').replace('\xa0','') if doc.find(class_='a-size-base') is not None else 0 for doc in docs]
           )

def read_info_byChannel(html):
    rank, title, href, asin, star, comments, price = get_info_byChannel(html)
    temp = pd.DataFrame({'rank':rank,
                         'title':title,
                         'href': href,
                         'asin': asin,
                         'star': star,
                         'comments': comments,
                         'price': price})
    return(temp)

