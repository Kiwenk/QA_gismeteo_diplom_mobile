import allure
from utils.methods_mobile import methods_gis_test


@allure.feature('Избранное')
@allure.story("Пользователь добавляет город в 'Избранное'")
@allure.label('gismeteo_modile_UI_favorites')
@allure.tag('favorites')
def test_add_city_to_favorite_section_from_city_page():
    methods_gis_test.favorite_check('Moscow')


@allure.feature('Избранное')
@allure.story("Пользователь добавляет город в 'Избранное' на главной странице")
@allure.label('gismeteo_modile_UI_favorites')
@allure.tag('favorites')
def test_add_city_to_favorite_section_from_main_page():
    methods_gis_test.favorite_check_from_main_page('Moscow')
