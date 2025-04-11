from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
#selecinando o navegador e abrindo o whatsapp
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get('https://web.whatsapp.com')

mensagem = '''Bom dia!
Estamos abertos das 7 às 19!
'''
import pyperclip

lista_contatos = ['eu (você)', 'penúltimo grupo', 'grupo bom',
'último grupo', 'nós e eu', 'automação']

#enviar a mensagem para eu (voce) para depois poder encaminhar

#clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
#escrever eu(voce)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p').send_keys('eu (você)')
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p').send_keys(Keys.ENTER)

#escrever a mensagem para nós mesmos
pyperclip.copy(mensagem)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL+'v')
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)

# encaminhar a mensagem para a lista de contatos
from selenium.webdriver.common.action_chains import ActionChains

#código para clicar no menu, aquela setinha na mensagem.

qtde_contatos = len(lista_contatos)

if qtde_contatos %5 ==0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    #rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    lista_elementos = nav.find_elements('class name', '_amk6')
    for item in lista_elementos:
        mensagem = mensagem.replace('\n', '')
        texto = item.text.replace('\n', '')
        if mensagem in texto:
            elemento = item

    # selecionar a mensagem para enviar e abre a caixa de encaminhar
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_ahkm').click()
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[5]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[2]/span').click()
    time.sleep(1)
   
    
    for nome in lista_enviar:
        # selecionar os 5 contatos para enviar
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(nome)
        time.sleep(1)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(Keys.ENTER)
        time.sleep(1)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)
    
qtde_contatos = len(lista_contatos)

if qtde_contatos %5 ==0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    #rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    lista_elementos = nav.find_elements('class name', '_amk6')
    for item in lista_elementos:
        mensagem = mensagem.replace('\n', '')
        texto = item.text.replace('\n', '')
        if mensagem in texto:
            elemento = item

    # selecionar a mensagem para enviar e abre a caixa de encaminhar
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_ahkm').click()
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[5]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[2]/span').click()
    time.sleep(1)
   
    
    for nome in lista_enviar:
        # selecionar os 5 contatos para enviar
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(nome)
        time.sleep(1)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(Keys.ENTER)
        time.sleep(1)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)