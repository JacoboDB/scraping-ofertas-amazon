import json 
import sys
from time import sleep
from amazon_scraper import AmazonScraper


HEADERS = {
            'authority': 'www.amazon.com.mx',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'User-Agent': 'Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US,es,es-MX;q=0.9,en;q=0.8',
        }
AMAZON_URL='https://www.amazon.com.mx'
AMAZON_SEARCH_URL='https://www.amazon.com.mx/s?k='


def main():
    validate_args()
    scrapper = AmazonScraper('products.yml')
    print('===============================INICIO===============================')
    process_search(scrapper)
    print('===============================FIN===============================')

def process_search(scrapper):
    search = sys.argv[1]
    discount = int(sys.argv[2])
    print(f'Buscando {search} con descuento de {discount}% ...')
    retries = 0
    url = AMAZON_SEARCH_URL + search.replace(' ','+')
    print(url)
    while retries < 5:
        data = scrapper.scrape(url, HEADERS)
        retries = examine_data(data, retries, discount)
    if (retries == 5):
        print(f'No se encontraron datos para la busqueda {search} después de {retries} reintentos')

def validate_args():
    if (len(sys.argv) == 0):
        raise Exception('No se proporcionó el producto a buscar')
    if (len(sys.argv) is not 3):
        raise Exception('Argumentos incorrectos: debe de ser [PRODUCTO] [DESCUENTO]. Ejemplo: "libro python" 20')

def print_product(product, price, regular, discount, percentage): 
    print('-------------------------------------------------------------------')
    print(f'Producto: {product["name"]}')
    print(f'Enlace: {AMAZON_URL + product["link"]}')
    print(f'Precio actual: {price}')
    print(f'Precio regular: {regular}')
    print(f'Descuento: ${discount:.0f} ({percentage:.0f}%)')

def examine_data(data, retries, discount_search):
    if data and data['products']:
        retries = 999
        for product in data['products']:
            if (product['regular-price'] and product['price']):
                regular = float(str(product['regular-price']).replace('$', '').replace(',', ''))
                price = float(str(product['price']).replace('$', '').replace(',', ''))
                discount = regular - price
                percentage = discount * 100 / regular
                if (percentage >= discount_search):
                    print_product(product, price, regular, discount, percentage)
    else:
        retries += 1
        sleep(5)
    return retries

if __name__ == '__main__':
    main()