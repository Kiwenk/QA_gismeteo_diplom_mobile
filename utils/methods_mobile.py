import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class GismeteoMethods:
    def __init__(self):
        pass

    def first_launch(self):
        browser.element((AppiumBy.ID, 'android:id/button1')).click()

    def open_city(self, city):
        with allure.step('Открываем страницу города через поиск'):
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/action_search')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type(f'{city}')
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()

    def name_check(self, city):
        with allure.step('Проверяем наименование города'):
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).element(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text(f'{city}'))

    def app_tab_visibility(self, tab):
        with allure.step('Проверяем видимость таба'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{tab}")')).should(be.visible)

    def app_tab_clickability(self, tab):
        with allure.step('Проверяем кликабельность таба'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{tab}")')).should(be.clickable)

    def more_options_visibility(self):
        with allure.step('Проверяем видимость "More options"'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).should(
                be.visible)

    def more_options_clickability(self):
        with allure.step('Проверяем кликабельность "More options"'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).should(
                be.clickable)

    def add_to_favorites(self):
        with allure.step('Добавляем город в "Избранное"'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("More options")')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add to favorites")')).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

    def city_in_favorites(self, city):
        with allure.step('Проверяем наличие города в "Избранное"'):
            browser.element(
                (AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).should(have.text(f'{city}'))

    def add_to_favorites_from_main_page(self, city):
        with allure.step('Добавляем город в "Избранное" на главной странице'):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.HorizontalScrollView[@resource-id="ru.gismeteo.gismeteo:id/tabTypeList"]/'
                             'android.widget.LinearLayout/android.support.v7.app.a.b[2]')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/fabAdd')).click()
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type(f'{city}')
            browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()


class test_interface_gis(GismeteoMethods):

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


methods_gis_test = test_interface_gis()
