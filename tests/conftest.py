import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support
import os
from appium import webdriver


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()


def attach_bstack_video(session_id):
    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('LOGIN'), os.getenv('KEY')),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


@pytest.fixture(autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': '10.0',
        'deviceName': 'Google Pixel 4',
        'app': 'bs://sample.app',
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': os.getenv('LOGIN'),
            'accessKey': os.getenv('KEY'),
        }
    })

    browser.config.driver = webdriver.Remote(
        'http://hub.browserstack.com/wd/hub',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    browser.quit()

    attach_bstack_video(session_id)
