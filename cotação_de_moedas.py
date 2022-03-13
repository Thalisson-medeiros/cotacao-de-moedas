import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
cotacao_dolar = cotacoes['USDBRL']['bid']

print('Cotação do Euro: ',cotacao_euro)
print('Cotação do Bitcoin: ',cotacao_bitcoin)
print('Cotação do Dólar: ',cotacao_dolar)
