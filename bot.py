from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from fractions import Fraction
import keyboard

def solve_method(before_answer, after_answer):
    opposite_operators = {"+": "-", "-": "+", "*": "/", "/": "*"}
    
    if len(after_answer) == 0:
        # composite fraction case 1/2 / 3/4 - PEMDAS not followed
        if before_answer.count("/") == 3:
            split = before_answer[:-2].split(" ")
            n1 = eval(split[0])
            n2 = eval(split[-1])
            return str(n1 / n2)
        
        # normal question (Easy Mode)
        return str(eval(before_answer[:-2]))
    
    if len(before_answer) == 0:
        # __ * 2 = 12
        split = after_answer.split("=")
        n1 = split[0]
        n2 = str(eval(split[-1]))
        operator = opposite_operators[n1[0]]
        n1 = str(eval(n1[1:]))
        return str(eval(n2 + operator + n1))
    
    # we have 3 * __ = 12 format
    operator = before_answer[-1]
    n1 = eval(before_answer[: - 1])
    n2 = eval(after_answer[2: ])
    if operator == "+": return str(n2 - n1)
    if operator == "-": return str(n1 - n2)
    if operator == "*": return str(n2 / n1)
    if operator == "/": return str(n1 / n2)
    
def solve(before_answer, after_answer):
    solution = solve_method(before_answer, after_answer)
    if int(float(solution)) == float(solution):
        return str(int(float(solution)))
    if len(solution) > 6:
        # too many decimals
        return str(Fraction(float(solution)).limit_denominator())
    return solution

def run(mode = "expert", turbo = True):
    # browser setup
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://rankyourbrain.com/mental-math/mental-math-test-" + mode + "/play")
    
    # getting HTML element that contains the question
    before_answer = browser.find_element_by_id("beforeAnswer")
    after_answer = browser.find_element_by_id("afterAnswer")
    
    # press space to start program once page opens (optionally - uncomment if you want to use this)
    '''while True:
        if keyboard.is_pressed(' '):
            break'''
    
    while True:
        try:
            solution = solve(before_answer.text, after_answer.text)
            if turbo:
                pyautogui.write(solution, _pause = False)
            else:
                # values 0.21 - 0.25 work well depending on mode
                pyautogui.write(solution, interval = 0.23, _pause = True)
        except: break
