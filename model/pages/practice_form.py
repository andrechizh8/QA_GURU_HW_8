from selene.support.shared import browser
from selene import be, have
from model.controls import datepicker, dropdown,check_box,radio_button
from model.utils import file_path, scroll


def open():
    browser.open('/automation-practice-form')


def type_firstname(firstname):
    browser.element('#firstName').should(be.blank).type(firstname)


def type_lastname(lastname):
    browser.element('#lastName').should(be.blank).type(lastname)


def type_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def select_gender(gender):
    radio_button.gender('[name=gender]',gender)


def type_phone_number(phone):
    browser.element('#userNumber').should(be.blank).type(phone)


def select_hobby(hobby):
    check_box.hobby('[for^=hobbies-checkbox]',hobby)


def type_address(address):
    scroll.scroll_to('#city')
    browser.element('#currentAddress').should(be.blank).type(address)


def select_date():
    browser.element('#dateOfBirthInput').click()


def select_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def select_month(month):
    browser.element('.react-datepicker__month-select').click()
    datepicker.select_date('.react-datepicker__month-select', month)


def select_year(year):
    browser.element('.react-datepicker__year-select').click()
    datepicker.select_date('.react-datepicker__year-select', year)


def select_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobbie(hobbie):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie)).click()


def picture_upload():
    file_path.create_path_to_file('#uploadPicture', 'resources\picture.png')


def select_state(state):
    dropdown.select('#state', state)


def select_city(city):
    dropdown.select('#city', city)


def click_submit():
    browser.element('#submit').press_enter()


def assert_info(*args):
    browser.element('.table').all('.table td:nth-child(2)').should(have.texts(args))


def click_close_button():
    scroll.scroll_to('#closeLargeModal')
    browser.element('#closeLargeModal').click()
