from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser):
    browser.get(link)
    try:
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-add-to-basket"))
        )
        return True
    except:
        return False

def test_for_different_languages(browser):
    assert is_element_present(browser)==True, "Корзина не найдена"
# конец

