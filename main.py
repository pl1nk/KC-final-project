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


xcite(product)