import pandas as pd
import win32com.client as win32

# importar a base de bados
tabela_vendas = pd.read_excel('vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)
print ('-'*50)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print ('-'*50)

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print ('-'*50)

# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# enviar um e-mail com relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'becka.devpython@outlook.pt'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>segue abaixo o relatório das vendas, listado por lojas:</p>

<p>FATURAMENTO</p>

{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>QUANTIDADE VENDIDA</p>

{quantidade.to_html()}

<p>TICKET MÉDIO</p>

{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att,</p>

<p>Rebeca Caroline</p>
  
'''

mail.Send()

print ('-'*50)
print ('Email enviado com sucesso')
