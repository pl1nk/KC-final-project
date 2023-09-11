from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}

product = input("What do u want? ")

xcite_url = f'https://www.xcite.com/search?q={product}&toggle%5BinStock%5D=true'

response = requests.get(xcite_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


product_divs = soup.find_all('div', class_='ProductTile_wrapperXPYR3')

if product_divs:
    for product_div in product_divs:
        title = product_div.find('p', class_='ProductTile_productNameR9tA5')
        price = product_div.find('span', class_='text-2xl text-functional-red-800 block mb-2')
        if title and price:
            title_text = title.text.strip()
            price_text = price.text.strip()
            print("Product Title:", title_text)
            print("Product Price:", price_text)
        else:
            print("Product title or price not fond")
    else:
        print("No products found on the page")
else:
    print("Failed to connect Status code:", response.status_code)