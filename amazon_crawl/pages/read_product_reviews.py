from amazon_crawl.process.process_reviews import get_review_info,get_review
from amazon_crawl.core.source_page import read_data_from, get_soup
import pandas as pd

def get_product_reviews(url, driver):
    title, cc, asin, oo, url_c = get_review_info(url)
    driver = read_data_from(driver, url_c)
    html = get_soup(driver)

    reviews = get_review(html)
    reviews = pd.DataFrame(reviews, columns=['title', 'date', 'star', 'body'])
    reviews = reviews.assign(asin= asin,
                             url = url)
    return(reviews)