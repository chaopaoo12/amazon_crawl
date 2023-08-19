

def get_category_info(html):

    if html.find('div',attrs={'role':"group"}).find_previous('div',attrs={'role':"treeitem"}) is not None:
        parent = html.find('div',attrs={'role':"group"}).find_previous('div',attrs={'role':"treeitem"}).text
    else:
        parent = 'root'

    category = [i.text for i in html.find('div',attrs={'role':"group"}).find_all('div',attrs={'role':"treeitem"})]
    href = [i.find('a').get('href') if i.find('a') is not None else None for i in html.find('div',attrs={'role':"group"}).find_all('div',attrs={'role':"treeitem"})]

    return(category, href, parent)



