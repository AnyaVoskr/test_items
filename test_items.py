from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_available_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    #button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    flag = False
    try:
        button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        button.click() 
    except NoSuchElementException:
        flag = True
    assert flag == False, f"Button 'Add to basket' is not found"


