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

    if product_divs:
     for product_div in product_divs:
        title = product_div.find('p', class_='ProductTile_productName__R9tA5')
        price = product_div.find('span', class_='text-2xl text-functional-red-800 block mb-2')
        parent = product_div.parent
        if title and price and parent:
            title_text = title.text.strip()
            price_text = price.text.strip()
            parent_text = parent.name.strip()
            
            parent = product_div.find_parent('a')
            
            if parent:
                link = parent['href']
                print("Product Title:", title_text)
                print("Product Price:", price_text)
                print("Product Link:", link)
                print()
                 
            else:
                print("Parent <a> tag not found")
        else:
            continue
    else:
     print("No products found on the page")


    response.close()





def eurika(product):
   
    

    params = {
        "x-algolia-agent": "Algolia for vanilla JavaScript (lite) 3.32.0;instantsearch.js (4.3.0);JS Helper (3.1.1)",
        "x-algolia-application-id": "5GPHMAA239",
        "x-algolia-api-key": "3d7dbc330852592da244c87ae924a221",
    }

    # Change the `query=charger` to put your query:
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

    for r in data["results"][0]["hits"]:
        print(
            f'{r["itmn"][:50]:<50} {r["clprcv"]:<10} https://www.eureka.com.kw/products/details/{r["objectID"]}'
        )




def blink(product):
    blink_url = f'https://www.blink.com.kw/en/Product/Products?searchText={product}&sortBy=&filterBy=cat:'
    response = requests.get(blink_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_divs = soup.find_all('div', class_='items')

    for product_div in product_divs:
        title = product_div.find('span', class_='item_name noSwipe')
        price = product_div.find('span', class_='newprice alignright bluetext')
        link = product_div.find('a')['href']

    if title and price and link:
        title_text = title.get_text(strip=True)
        price_text = price.get_text(strip=True)
        print("Product Title:", title_text)
        print("Product Price:", price_text)
        print("Product Link:", link)
        print()
    else:
        print("Product information not found in one of the product divs.")


xcite(product)
eurika(product)
    


