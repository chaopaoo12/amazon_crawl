from amazon_crawl.multi.process.process_channel import process_channel
import multiprocessing
import pandas as pd

def mult_channel_process(df):
    pool = multiprocessing.Pool(15)
    with pool as p:
        res = p.map(process_channel, [tuple(x) for x in df[['url', 'channel', 'parent']].values])
    return(pd.concat(res))