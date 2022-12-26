import model
from model.pages import practice_form


def test_form_filling():
    practice_form.open()

    practice_form.type_firstname('Andrew')
    practice_form.type_lastname('Chizh')
    practice_form.type_email('andrechizh.ru@yandex.ru')

    practice_form.select_gender('Male')

    practice_form.type_phone_number('9183346139')

    practice_form.select_date()
    practice_form.select_month('December')
    practice_form.select_year('1992')
    practice_form.select_day('08')

    practice_form.select_subject('Math')

    practice_form.select_hobbie('Music')

    practice_form.picture_upload()

    practice_form.type_address('Krasnodar')

    practice_form.select_state('Haryana')
    practice_form.select_city('Karnal')
    practice_form.click_submit()

    practice_form.assert_info(
        'Andrew Chizh',
        'andrechizh.ru@yandex.ru',
        'Male',
        '9183346139',
        '08 December,1992',
        'Math',
        'Music',
        'picture.png',
        'Krasnodar',
        'Haryana Karnal'
    )


    practice_form.click_close_button()
