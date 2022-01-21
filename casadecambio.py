import requests

requisicaodolar = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
cotdolar = requisicaodolar.json()
r = float(input('Insira o valor R$: '))
print('-'*50)
print('*****Cotação do Dólar*****')
print('A cotação do dolar de hoje é US$:', cotdolar['USDBRL']['high'])
d = float(cotdolar['USDBRL']['high'])
dolar = r/d
print('Você pode comprar US$ {:.2f} dolares'.format(dolar))

requisicaoeuro = requests.get('http://economia.awesomeapi.com.br/json/last/EUR-BRL')
coteuro = requisicaoeuro.json()
print('-'*50)
print('*****Cotação do Euro*****')
print('A cotação do euro de hoje é €$:', coteuro['EURBRL']['high'])
e = float(coteuro['EURBRL']['high'])
euro = r/e
print('Você pode comprar €$ {:.2f} euros'.format(euro))

requisicaolibra = requests.get('http://economia.awesomeapi.com.br/json/last/GBP-BRL')
cotlibra = requisicaolibra.json()
print('-'*50)
print('*****Cotação da Libra*****')
print('A cotação da libra de hoje é £:', cotlibra['GBPBRL']['high'])
l = float(cotlibra['GBPBRL']['high'])
libra = r/l
print('Você pode comprar £ {:.2f} libra'.format(libra))
