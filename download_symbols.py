from bs4 import BeautifulSoup
import requests

alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M',
            'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z')
exchanges = ('NYSE', 'NASDAQ')


def put_symbols_in_file(symbols):
    url = 'http://www.eoddata.com/stocklist/{0}/{1}.htm'
    for exchange in exchanges:
        for letter in alphabet:
            page = requests.get(url.format(exchange, letter))
            contents = page.content
            soup = BeautifulSoup(contents, 'html.parser')
            links = soup.find_all('a')
            for soupy in links:
                link = soupy.get('href')
                if '/stockquote/{}/'.format(exchange) in link:
                    if link[13 + len(exchange):-4] not in symbols:
                        symbols.append(link[13 + len(exchange):-4])
    text_file = open('./data_files/symbols.txt', 'w+')

    for symbol in symbols:
        text_file.write(symbol + '|')
    text_file.close()


def load_symbols_from_file():
    text_file = open('./data_files/symbols.txt', 'r')
    text = text_file.read()
    symbols = filter(None, text.split('|'))
    text_file.close()
    return symbols


def sort_symbols_file():
    symbols = load_symbols_from_file()
    open('symbols.txt', 'w').close() #clear the text file
    symbols.sort()
    text_file = open('./data_files/symbols.txt', 'w+')
    for symbol in symbols:
        text_file.write(symbol + '|')
    text_file.close()


def main():
    put_symbols_in_file(load_symbols_from_file())
    sort_symbols_file()


if __name__ == "__main__":
    main()