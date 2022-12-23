from selene.support.shared import browser
from selene import be,have

def select_date(selector,value):
    browser.element(selector).all('option').element_by(have.text(value)).click()
