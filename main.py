from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
}

product = input("What do you want? ")

def xcite(product) :
    xcite_url = f'https://www.xcite.com/search?q={product}&hierarchicalMenu%5Bcategories.lvl0%5D=Best%20Sellers&toggle%5BinStock%5D=true'

    response = requests.get(xcite_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_divs = soup.find_all('div', class_='ProductTile_wrapper__XPYR3')
    cheapest_xcite_product = None

    if product_divs:
     for product_div in product_divs:
        title = product_div.find('p', class_='ProductTile_productName__R9tA5')
        price = product_div.find('span', class_='text-2xl text-functional-red-800 block mb-2')
        parent = product_div.parent
        if title and price and parent:
            title_text = title.text.strip()
            price_text = price.text.strip()
            price_text = price_text.replace(' KD', '').strip()  
            parent_text = parent.name.strip()
            
            parent = product_div.find_parent('a')
            
            if parent:
                    link = parent['href']
                    xcite_product = {
                        'title': title_text,
                        'price': price_text,
                        'link': link,
                    }
                    if cheapest_xcite_product is None or float(price_text) < float(cheapest_xcite_product['price']):
                        cheapest_xcite_product = xcite_product
            else:
                print("Parent <a> tag not found")
        else:
            continue
    
    return cheapest_xcite_product


    





def eurika(product):
   
    

    params = {
        "x-algolia-agent": "Algolia for vanilla JavaScript (lite) 3.32.0;instantsearch.js (4.3.0);JS Helper (3.1.1)",
        "x-algolia-application-id": "5GPHMAA239",
        "x-algolia-api-key": "3d7dbc330852592da244c87ae924a221",
    }

    
    payload = {
        "requests": [
            {
                "indexName": "instant_records",
                "params": f"hitsPerPage=25&distinct=true&clickAnalytics=true&query={product}&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&maxValuesPerFacet=300&page=0&facets=%5B%22bn%22%2C%22clprc%22%2C%22rmn%22%5D&tagFilters=",
            }
        ]
    }

    api_url = "https://5gphmaa239-dsn.algolia.net/1/indexes/*/queries"

    data = requests.post(api_url, params=params, json=payload).json()
    cheapest_eurika_product = None

    for r in data["results"][0]["hits"]:
        title = r["itmn"]
        price = r["clprcv"]
        link = f'https://www.eureka.com.kw/products/details/{r["objectID"]}'

        eurika_product = {
            'title': title,
            'price': price,
            'link': link,
        }

        if cheapest_eurika_product is None or float(price) < float(cheapest_eurika_product['price']):
            cheapest_eurika_product = eurika_product

    return cheapest_eurika_product




xcite(product)
eurika(product)
cheapest_xcite = xcite(product)
cheapest_eurika = eurika(product)

if cheapest_xcite and cheapest_eurika:
    if float(cheapest_xcite['price'].replace('KWD', '').strip()) < float(cheapest_eurika['price']):
        print("Cheapest Product (Xcite):")
        print("Title:", cheapest_xcite['title'])
        print("Price:", cheapest_xcite['price'])
        print("Link:", cheapest_xcite['link'])
    else:
        print("Cheapest Product (Eureka):")
        print("Title:", cheapest_eurika['title'])
        print("Price:", cheapest_eurika['price'])
        print("Link:", cheapest_eurika['link'])
elif cheapest_xcite:
    print("Cheapest Product (Xcite):")
    print("Title:", cheapest_xcite['title'])
    print("Price:", cheapest_xcite['price'])
    print("Link:", cheapest_xcite['link'])
elif cheapest_eurika:
    print("Cheapest Product (Eureka):")
    print("Title:", cheapest_eurika['title'])
    print("Price:", cheapest_eurika['price'])
    print("Link:", cheapest_eurika['link'])
else:
    print("No products found on both websites.")
    


