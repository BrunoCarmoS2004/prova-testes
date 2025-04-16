#Todos os importes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

#Aqui criamos uma instacia para o webdriver do Chrome.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


try:
    #Aqui nos definimos o site
    url = "https://www.hankeds.com.br/prova/login.html"
    #Aqui nós pedimos para o drive carregar a url.
    driver.get(url)

    #Temos que colocar um delay para o drive carregar
    time.sleep(2)

    #Aqui criamos uma função para digirar os dados nos campos, isso com um delay para não dar problema.
    def digitar_lento(elemento, texto, delay=0.25):
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(delay)

    #Aqui criamos uma simulação de um usuario
    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    #Aqui buscamos os elementos pelo id 
    senha = driver.find_element(By.ID, "password")
    botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

    #Aqui digitamos nos campos os textos definidos para o teste de login, isso com um delei
    digitar_lento(usuario, "admin")
    time.sleep(1)
    digitar_lento(senha, "admin123456")
    time.sleep(1)

    #Aqui clicamos no botão para testar o botão de login
    botao.click()
    time.sleep(4)

    #Aqui verificamos se o botão nos levou para a pagina certa
    if "destino.html" in driver.current_url:
        #Se o teste nos levar para a pagina certa, ele mostra esse print no console
        print(" Teste passou: redirecionado corretamente.")
    else:
        #Se não levar para essa tela ele da erro e mostra esse print
        print(" Teste falhou: redirecionamento não ocorreu.")

    #Aqui espera mais um tempo para finalizar os processos 
    time.sleep(5)

#Caso der erro no meio do teste por causa de alguma variavel ou definição ele entra nessa excption
except Exception as e:
    print(" Erro durante o teste:", str(e))

#Aqui fecha o navegador e finaliza a execução do drive
finally:
    driver.quit()

