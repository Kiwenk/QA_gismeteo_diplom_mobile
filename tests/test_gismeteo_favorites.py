import allure
from utils.methods_mobile import gis_met


@allure.feature('Избранное')
@allure.story("Пользователь добавляет город в 'Избранное'")
@allure.label('gismeteo_modile_UI_favorites')
@allure.tag('favorites')
def test_add_city_to_favorite_section_from_city_page():
    gis_met.favorite_check('Moscow')


@allure.feature('Избранное')
@allure.story("Пользователь добавляет город в 'Избранное' на главной странице")
@allure.label('gismeteo_modile_UI_favorites')
@allure.tag('favorites')
def test_add_city_to_favorite_section_from_main_page():
    gis_met.favorite_check_from_main_page('Moscow')
