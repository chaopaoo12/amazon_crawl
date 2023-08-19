

def get_review_info(url):
    title, cc, asin, oo = url.split('/')
    url_c = 'https://www.amazon.com/{title}/product-reviews/{asin}/reviewerType=all_reviews&pageNumber={page_num}&sortBy=recent'.format(title=title, asin=asin)
    return(title, cc, asin, oo, url_c)

def get_review(html):
    docs = html.find_all(attrs={'class':'a-section review aok-relative'})
    return([doc.find(attrs={'data-hook':'review-title'}).span.text for doc in docs],
           [doc.find(attrs={'data-hook':'review-date'}).text for doc in docs],
           [doc.find(attrs={'data-hook':'review-star-rating'}).text for doc in docs],
           [doc.find(attrs={'data-hook':'review-body'}).span.text for doc in docs]
           )
