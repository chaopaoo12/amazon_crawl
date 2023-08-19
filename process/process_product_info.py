
def get_fivepoints(html):
    five_points = ''.join([i.text for i in html.find('div',{'id':['feature-bullets']}).find_all(attrs={'class':'a-list-item'})])
    return(five_points)

def get_labels(html):

    if html.find('div',{'id':['detailBullets_feature_div']}) is not None:
        labels = [i.find_all('span')[1].text.replace('\n','').replace('\u200f','').replace('\u200e','').replace('  ','') for i in html.find('div',{'id':['detailBullets_feature_div']}).find_all('li')]
        values = [i.find_all('span')[2].text.replace('\n','').replace('\u200f','').replace('\u200e','').replace('  ','') for i in html.find('div',{'id':['detailBullets_feature_div']}).find_all('li')]
    elif html.find('table',{'id':['productDetails_detailBullets_sections1']}) is not None:
        labels = [i.find('th').text.replace('\n','') for i in html.find('table',{'id':['productDetails_detailBullets_sections1']}).find_all('tr')]
        values = [i.find('td').text.replace('\n','') for i in html.find('table',{'id':['productDetails_detailBullets_sections1']}).find_all('tr')]

    res_d = {labels[i]: values[i] for i in range(len(labels))}
    return(res_d)

