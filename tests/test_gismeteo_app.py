import allure
import pytest
from utils.methods_mobile import gis_met


@pytest.mark.parametrize('city', ['Moscow', 'Beijing', 'Paris', 'Los Angeles', 'Dubai', 'Tokyo'])
def test_search_check(city):
    gis_met.check_search(city)


@pytest.mark.parametrize('tab', ['HOURS', 'DAYS'])
def test_android_ui_tabs_hours_check(tab):
    gis_met.tabs_check('Moscow', tab)


def test_android_ui_more_options_button():
    gis_met.more_options_check('Moscow')


def test_add_city_to_favorite_section_from_city_page():
    gis_met.favorite_check('Moscow')


def test_add_city_to_favorite_section_from_main_page():
    gis_met.favorite_check_from_main_page('Moscow')
