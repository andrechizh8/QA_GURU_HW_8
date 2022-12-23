import os
from selene.support.shared import browser

def create_path_to_file(selector,path):
    browser.element(selector).send_keys(
        os.path.join(os.path.dirname(__file__),path)
    )

