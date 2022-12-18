from selenium import webdriver

driver = webdriver.Firefox() # Open Firefox
driver.get("https://www.whdownload.com/games.php?name=%&sort=0&dir=0") # Open website

i = 2

while 1:    
    xpath_element = '/html/body/font/table[3]/tbody/tr['+ str(i) +']/td[1]/a'
    i = i + 1
    if xpath_element == "/html/body/font/table[3]/tbody/tr[3392]/td[1]/a":
        break
    game = driver.find_element("xpath", xpath_element)
    game.click()

"""
Last Game:
"/html/body/font/table[3]/tbody/tr[3392]/td[1]/a"
"""
