# Проект по автоматизации тестирования UI мобильного приложения Gismeteo
<a target="_blank" href="https://www.gismeteo.ru/soft-mobile/">Сайт проекта</a>

## 📄 Содержание
- [Технологии и инструменты](#tech_and_ins-технологии-и-инструменты)
- [Примеры UI тестов](#pager-Примеры-UI-тестов)
- [Сборка в Jenkins](#-Сборка-в-Jenkins)
- [Allure отчет](#-Allure-отчет)
- [Отчет в Telegram с помощью бота](#-Отчет-в-Telegram-с-помощью-бота)
- [Видео прохождения тестов на BrowserStack](#film_projector-Видео-прохождения-тестов-на-BrowserStack)

## :wrench: Технологии и инструменты
<p>
<a href="https://www.python.org/"><img src="resources/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/PyCharm_Icon.svg" width="50" height="50"  alt="Pycharm" title="IntelliJ IDEA"/></a>
<a href="https://github.com/"><img src="resources/Github.svg" width="50" height="50"  alt="Github" title="GitHub"/></a>
<a href="https://www.selenium.dev/"><img src="resources/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://appium.io/"><img src="resources/appium-logo-white.png" width="50" height="50"  alt="Appium" title="Appium"/></a>
<a href="https://www.browserstack.com/"><img src="resources/browserstack.png" width="50" height="50"  alt="Selenoid" title="browserstack"/></a>
<a href="https://www.jenkins.io/"><img src="resources/Jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/Allure_Report.svg" width="50" height="50"  
alt="Allure" title="Allure"/></a>
<a href="https://telegram.org/"><img src="resources/Telegram.svg" width="50" height="50"  alt="Telegram" title="Telegram"/></a>
<a href="https://qameta.io/"><img src="resources/Allure_Testops.svg" width="50" height="50"  alt="Allure_Test_Ops" title="Allure_Test_Ops"/></a>



В данном проекте автотесты написаны на <code>Python</code> с использованием <code>BrowserStack</code>, <code>Appium</code> и <code>Pytest</code> для UI-тестов
>
> <code>BrowserStack</code> выполняет запуск браузеров на отдельных удалённых смартфонах под управлением ОС <code>Android</code>.
>
> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.


## :pager: Примеры UI тестов
- Проверка добавления города в "Избранное"
- Проверка работоспособности поиска
- Проверка корректности наименования заголовка страницы с городом
- Проверка навигационого бара
- Проверка работоспособности кнопки "More options" 


## <img src="resources/Jenkins.svg" width="25" height="25"  alt="Jenkins" title="Jenkins"/></a> Сборка в Jenkins с параметрами
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>. 
>
>Также реализованы конфиги с запуском тестов на физическом устройстве и эмуляторе Android (Примечание: только локальный запуск!).
>
>Для изменения конфига необходимо при запуске тестов через pytest указать параметр context <code> pytest --context=local </code>.
>
>По умолчанию используется конфиг <code>BrowserStack</code>
>
> Запуск джоба происходит по нажатию кнопки <code>Build now</code>

<p align="center">
<img title="Сборка в Jenkins" src="resources/Jenkins_parametrs.png">
</p>

## <img src="resources/Allure_Report.svg" width="25" height="25"  alt="Allure_Report" title="Allure_Report" title="Allure_Report"/></a> Allure отчет
>
> Allure формирует подробный отчет о прогоне тестов. Кастомные фильтры и листенеры делают отчет максимально понятным
>
> Например отчеты формируются по категориям, в конце приложен скриншот, видео запись прогона теста и XML документ.
<p align="center">
<img title="Allure отчет" src="resources/Allure_Overview.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_suites.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_graphs.png">
</p>

## <img width="4%" title="Telegram" src="resources/Telegram.svg"> Отчет в Telegram с помощью бота
>
> После прогона всех тестов в <code>Telegram</code> чат автоматически приходит сообщение с полной информацией о прогоне и ссылкой на <code>Allure</code>
>
<p>
<img title="Отчет в Telegram с помощью бота" src="resources/Telegram_results.png">
</p>

## :film_projector: Видео прохождения тестов на BrowserStack
>
> <code>BrowserStack</code> пишет видео прогона каждого теста и видео прикладывается в отчет <code>Allure</code>
>
<p>
<img title="BrowserStack Video" src="resources/video_test.gif" alt="video">
</p>
