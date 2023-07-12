from lib2to3.pgen2 import driver
import random
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os
import warnings

# Знаю, что может скрыть другие потенциально важные сообщения об ошибках
warnings.filterwarnings("ignore", category=DeprecationWarning, module="urllib3")
warnings.filterwarnings("ignore", category=ResourceWarning)

load_dotenv() # Подгрузка переменных окружений

# Установите путь к веб-драйверу Chrome или Firefox
webdriver_service = Service('driver/chromedriver')


driver = webdriver.Chrome(service=webdriver_service)  # Убедитесь, что у вас установлен Chrome WebDriver и указан правильный путь к нему

# Перейти на страницу
driver.get("http://www.pdd24.com/for-school")

# Ввожу данные
last_input = driver.find_element(By.ID, "textSchoolName1")
first_input = driver.find_element(By.ID, "textSchoolName2")
midle_input = driver.find_element(By.ID, "textSchoolName3")
last_input.send_keys(os.getenv("LASTNAME"))
first_input.send_keys(os.getenv("FIRSTNAME"))
midle_input.send_keys(os.getenv("MIDDLENAME"))
print(f"Ввожу данные: ФИО и почту учителя")

driver.find_element(By.ID, "examSize80").click() 
driver.find_element(By.ID, "examSize100").click()
driver.find_element(By.ID, "emailResult").click()
driver.find_element(By.ID, "emailResult").send_keys(os.getenv("EMAILTEACHER"))

driver.find_element(By.ID, "buttonSchoolSetName").click()

wait = WebDriverWait(driver, 50)
counter = 0
while True:    
    
    wait_time = random.randint(15, 65)
    print(f"Ожидаю {wait_time} сек.")
    time.sleep(wait_time)
    
    counter += 1
    print(f"Начинаю решать. Вопрос - {counter}")
    
    questionElement1 = driver.find_element(By.ID, "labelQuestNumber")
    text = questionElement1.text
    # Б40 В2
    pattern = r"Б(\d+) В(\d+)"
    match = re.match(pattern, text)
    if match:
    # Получаем значения чисел из соответствия
        b_value = int(match.group(1))
        v_value = int(match.group(2))

    # Создаем переменные вида B = 40, V = 2
        locals()["B"] = b_value
        locals()["V"] = v_value

        print(f'Билет № {B}. Вопрос №{V}')
        print(f'Ищу ответ на drom.ru (https://www.drom.ru/pdd/bilet_{B}/#{V})')  # Выводит: 2  
    else:
        print("Не найдено соответствие шаблону")
          
    # https://www.drom.ru/pdd/bilet_40/#2

    driver.execute_script("window.open('about:blank', 'newtab')")
    handles = driver.window_handles
    first_tab = handles[0]
    second_tab = handles[1]
    driver.switch_to.window(second_tab)

    driver.get(f'https://www.drom.ru/pdd/bilet_{B}/#{V}')

    element = driver.find_element(By.CSS_SELECTOR, f'a[data-show-answer="{V}"]')
    element.click()
    element = driver.find_element(By.ID,f"c{V}")

    text = element.text
    # Использование регулярного выражения для поиска числа после "Правильный ответ:"
    pattern = r"Правильный ответ: (\d+)"
    match = re.search(pattern, text)

    if match:
        answer = int(match.group(1))
        # Вывод числа
        print(f'Ответ: {answer}')
    else:
        print("Ответ не найден")

    driver.close()    
    driver.switch_to.window(first_tab)    
    element = driver.find_element(By.XPATH, f'//a[@data-num="{answer}"]')
    element.click()
    print("Перехожу к следующему вопросу")
    
    try:
        element = driver.find_element(By.XPATH,"//div[@id='resultPanel' and not(contains(@class, 'hide'))]")
        print("Экзамен закончен")
        wait = input("Нажми Enter чтобы выйти!")
        print("Bye-Bye c:")
        driver.quit()
        exit()
    except NoSuchElementException:
        print("")
    

        
    