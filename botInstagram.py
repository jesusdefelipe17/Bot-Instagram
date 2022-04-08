from pathlib import Path
import time

from selenium import webdriver

Path = 'chromedriver.exe'
web = webdriver.Chrome(Path)

user = 'USUARIO'
password = 'PASSWORD'
url="NOMBRE USUARIO AL QUE COPIAR LOS FOLLOWERS"
def login():
    
    web.get('http://instagram.com')
    time.sleep(2)
    web.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    time.sleep(2)
    web.find_element_by_name('username').send_keys(user)
    web.find_element_by_name('password').send_keys(password)
    time.sleep(1)
    web.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
    time.sleep(5)

def abrirSeguidores(account_instagram):

    web.get("https://www.instagram.com/" + account_instagram + "/followers/")
    time.sleep(2)
    web.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()




def recorrer_Seguidores(minutos):
    time.sleep(2)
    pop_up_window = web.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
    # Scroll till Followers list is there
    timeout = time.time() + 60 * minutos
    while True:
        if time.time() > timeout:
            break
        web.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
            pop_up_window)
        time.sleep(1)


def follow_followers():
    list_followers = web.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul")
    contador=0
    for child in list_followers.find_elements_by_css_selector("li"):
        user_name = child.find_element_by_css_selector(".notranslate").text
        follow_button = child.find_element_by_css_selector("button")
        print(user_name)
        print("----")
        print(follow_button.text)
        if "Seguir" == follow_button.text:
            follow_button.click()
            print(user_name + "seguido")
            contador+=1
            print("Seguidor Nº: "+str(contador))
        else:
            print("Ya lo sigues")
        time.sleep(1)
        if contador==150:
         break

login();
abrirSeguidores(url)
recorrer_Seguidores(1)
follow_followers()
