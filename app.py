import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opts)
url = 'https://mercadolivre.com.br'
navegador.get(url)

# Aguarda a página carregar
time.sleep(3)

campo_pesquisar = navegador.find_element(By.TAG_NAME, "input")
campo_pesquisar.send_keys("Notebook Dell G15")
campo_pesquisar.send_keys(Keys.RETURN)

# Aguarda a pesquisa carregar
time.sleep(3)

# Abre a página do produto
url = 'https://produto.mercadolivre.com.br/MLB-3891159509-notebook-dell-gamer-g15-5530-i5-13450hx-16gb-512gb-rtx-3050-_JM?searchVariation=182050720100'
navegador.get(url)

# Aguarda a página do produto carregar
time.sleep(3)

# Localiza o elemento do preço
preco_elemento = navegador.find_element(By.XPATH, '//*[@id="price"]/div/div[1]/div[1]/span/span/span[2]')

preco = preco_elemento.text

preco_limpo = preco.replace('R$', '').replace('.', '').replace(',', '.').strip()

preco_float = float(preco_limpo)


url = "https://www.mercadolivre.com.br/notebook-dell-inspiron-i15-i120k-a30pf-i5-16gb-512-156-w11/p/MLB29263176#polycard_client=search-nordic&wid=MLB3878467791&sid=search&searchVariation=MLB29263176&position=15&search_layout=grid&type=product&tracking_id=80fb6f71-ca0a-417e-ba6e-00934ee737af"
navegador.get(url)
time.sleep(3)
preco_elemento = navegador.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]')
preco = preco_elemento.text
preco_limpo = preco.replace('R$', '').replace('.', '').replace(',', '.').strip()
preco_float = float(preco_limpo)


url = "https://www.mercadolivre.com.br/notebook-gamer-dell-g15-i1300-a46p-i5-16gb-512gb-rtx4050-w11/p/MLB38834673#wid%3DMLB4994836550%26sid%3Dsearch%26searchVariation%3DMLB38834673%26position%3D9%26search_layout%3Dgrid%26type%3Dproduct%26tracking_id%3D00332656-3cbe-4a97-9bec-658492c3ce33"
navegador.get(url)
time.sleep(3)
preco_elemento = navegador.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]')
preco = preco_elemento.text
preco_limpo = preco.replace('R$', '').replace('.', '').replace(',', '.').strip()
preco_float = float(preco_limpo)


caminho_arquivo = 'preco_notebook.txt'
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(f'Preço do Notebook Dell G15: R$ {preco_float:.2f}')
    arquivo.write(f'Preço do Notebook Dell G15: R$ 6.800')
    arquivo.write(f'Preço do Notebook Dell G15: R$ 8.599')



subprocess.run(['notepad.exe', caminho_arquivo])

print(preco_float)

navegador.quit()

