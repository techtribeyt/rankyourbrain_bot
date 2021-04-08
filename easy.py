from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

# browser setup
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://rankyourbrain.com/mental-math/mental-math-test-easy/play")

# getting HTML element that contains the question
question_element = browser.find_element_by_id("beforeAnswer")

while True:
    # here, we take away the "=", evaluate the expression, round down to nearest int and convert to string
    # then, we type it in
    try:
        # use this line to get a legal score (under 200 points)
        # pyautogui.write(str(int(eval(question_element.text[:-2]))), interval = 0.23, _pause = True)
        
        # use this line for super super super fast illegal score
        pyautogui.write(str(int(eval(question_element.text[:-2]))), _pause = False)
    except: break
