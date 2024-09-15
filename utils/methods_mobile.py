import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class GismeteoMethods:
    def __int__(self):
        pass

    def first_launch(self):
        browser.element((AppiumBy.ID, 'android:id/button1')).click()

    with allure.step('Открываем страницу города через поиск'):
        def open_city(self, city):
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/action_search')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type(f'{city}')
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()

    with allure.step('Проверяем наименование города'):
        def name_check(self, city):
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).element(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text(f'{city}'))

    with allure.step('Проверяем видимость таба'):
        def app_tab_visibility(self, tab):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{tab}")')).should(be.visible)

    with allure.step('Проверяем кликабельность таба'):
        def app_tab_clickability(self, tab):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{tab}")')).should(be.clickable)

    with allure.step('Проверяем видимость "More options"'):
        def more_options_visibility(self):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).should(
                be.visible)
    with allure.step('Проверяем кликабельность "More options"'):
        def more_options_clickability(self):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).should(
                be.clickable)

    with allure.step('Добавляем город в "Избранное"'):
        def add_to_favorites(self):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add to favorites")')).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

    with allure.step('Проверяем наличие города в "Избранное"'):
        def city_in_favorites(self, city):
            browser.element(
                (AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).should(have.text(f'{city}'))

    with allure.step('Добавляем город в "Избранное" на главной странице'):
        def add_to_favorites_from_main_page(self, city):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.HorizontalScrollView[@resource-id="ru.gismeteo.gismeteo:id/tabTypeList"]/'
                             'android.widget.LinearLayout/android.support.v7.app.a.b[2]')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/fabAdd')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type(f'{city}')
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()

    # поискать как перенести методы в наследуемый класс. Сделать из этого интерфейс для теста
    # (проблема: не могу перенести параметризацию в родительский класс)

    @allure.description('Проверка работы поиска поиска')
    @allure.severity(allure.severity_level.BLOCKER)
    def check_search(self, city):
        self.first_launch()
        self.open_city(city)
        self.name_check(city)

    @allure.description('Проверка работы табов')
    @allure.severity(allure.severity_level.CRITICAL)
    def tabs_check(self, city, tab):
        self.first_launch()
        self.open_city(city)
        self.app_tab_visibility(tab)
        self.app_tab_clickability(tab)

    @allure.description('Проверка кнопки "More options"')
    @allure.severity(allure.severity_level.CRITICAL)
    def more_options_check(self, city):
        self.first_launch()
        self.open_city(city)
        self.more_options_visibility()
        self.more_options_clickability()

    @allure.description('Проверка добавления города в "Избранное')
    @allure.severity(allure.severity_level.CRITICAL)
    def favorite_check(self, city):
        self.first_launch()
        self.open_city(city)
        self.add_to_favorites()
        self.city_in_favorites(city)

    @allure.description('Проверка Проверка добавления города в "Избранное с главной страницы')
    @allure.severity(allure.severity_level.CRITICAL)
    def favorite_check_from_main_page(self, city):
        self.first_launch()
        self.add_to_favorites_from_main_page(city)
        self.city_in_favorites(city)


gis_met = GismeteoMethods()
