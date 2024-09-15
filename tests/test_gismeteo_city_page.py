import pytest
import allure
from utils.methods_mobile import gis_met


@allure.feature('Табы')
@allure.story("Пользователь хочет поменять вкладку на странице города")
@allure.label('gismeteo_modile_UI_nav_buttons')
@allure.tag('nav_buttons')
@pytest.mark.parametrize('tab', ['HOURS', 'DAYS'])
def test_android_ui_tabs_hours_check(tab):
    gis_met.tabs_check('Moscow', tab)


@allure.feature('Табы')
@allure.story("Пользователь нажимает на кнопку 'More options'")
@allure.label('gismeteo_modile_UI_more_options_button')
@allure.tag('more_options')
def test_android_ui_more_options_button():
    gis_met.more_options_check('Moscow')
