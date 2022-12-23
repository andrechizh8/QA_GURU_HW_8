from selene import be,have
from selene.support.shared import browser

def select(seletor, text):
    browser.element(seletor).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)
    ).click()