import pytest
import allure
from utils.methods_mobile import methods_gis_test


@allure.feature('Поиск')
@allure.story("Пользователь ищит город через поиск")
@allure.label('gismeteo_modile_UI_search')
@allure.tag('search')
@pytest.mark.parametrize('city', ['Moscow', 'Beijing', 'Paris', 'Los Angeles', 'Dubai', 'Tokyo'])
def test_search_check(city):
    methods_gis_test.check_search(city)
