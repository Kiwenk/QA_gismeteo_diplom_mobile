import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.story("Запускаем приложение Википедии в первый раз")
@allure.severity(allure.severity_level.CRITICAL)
def test_getting_started():
    with allure.step('Проверяем первую страницу'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(
            have.text('We’ve found the following on your device:'))
    with allure.step('Проверяем вторую страницу'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
    with allure.step('Проверяем третью страницу'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
    with allure.step('Проверяем четвёртую страницу'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))


@allure.story("Ищем в википедии Appium")
def test_search():
    with step('Вводим "Appium" в поиске Википедии'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Проверяем наименование результата'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.story("Ищем в википедии Devil May Cry и кликаем его")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_first_article_DMC():
    with step('Вводим "Devil May Cry" в поиске Википедии'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Devil May Cry')

    with step('Проверяем наименование результата'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Devil May Cry'))

    with step('Кликаем элемент'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
