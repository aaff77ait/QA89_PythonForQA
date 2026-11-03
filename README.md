# QA89_PythonForQA
QA Python Automation Project
📌 О проекте (About the Project)
Учебный проект по автоматизации тестирования веб-приложения с использованием Python и pytest.
Тестируемый продукт: Demo Web Shop
Ссылка: https://demowebshop.tricentis.com/
Цель проекта: научиться создавать автоматизированные тесты, выполнять проверки через assertions, запускать тесты и хранить проект в GitHub.
🛠 Технологии (Tech Stack)
Python 3
pytest
Selenium WebDriver
Git / GitHub
PyCharm
Google Chrome
📁 Структура проекта (Project Structure)
QA_Python_Automation/
├── tests/
│   ├── test_login.py
│   └── test_homepage.py
├── requirements.txt
├── .gitignore
└── README.md
🚀 Установка и запуск (Getting Started)
1. Клонировать репозиторий
git clone https://github.com/USERNAME/QA_Python_Automation.git
cd QA_Python_Automation
Замените USERNAME на свой GitHub username. Репозиторий должен быть предварительно создан.
2. Создать виртуальное окружение
Windows:
python -m venv .venv
.venv\Scripts\activate
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Установить библиотеки
python -m pip install -r requirements.txt
Файл requirements.txt:
pytest
selenium
4. Запустить тесты
python -m pytest -v
🧪 Тестовые сценарии (Test Scenarios)
ID
Test Case
Expected Result
TC-01
Open Home Page
Главная страница открывается
TC-02
Check Page Title
Заголовок соответствует ожидаемому
TC-03
Open Login Page
Открывается страница Login
TC-04
Login with Valid Credentials
Пользователь успешно авторизован
TC-05
Login with Invalid Credentials
Появляется сообщение об ошибке

Для TC-04 необходима предварительно зарегистрированная тестовая учетная запись.
✅ Пример автоматизированного теста
Файл tests/test_homepage.py:
from selenium import webdriver

def test_homepage_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demowebshop.tricentis.com/")

        assert "Demo Web Shop" in driver.title

    finally:
        driver.quit()
📊 Test Results
После запуска тестов pytest показывает результаты в терминале.
PASSED — тест успешно выполнен.
FAILED — проверка не прошла.
ERROR — возникла ошибка при подготовке или выполнении теста.
📋 Правила работы над проектом
Создать репозиторий на GitHub.
Клонировать проект в PyCharm.
Создать виртуальное окружение.
Установить необходимые библиотеки.
Создать папку tests.
Написать автоматизированные тесты.
Выполнить проверки с помощью assert.
Запустить тесты через pytest.
Сохранить изменения с помощью Git commit.
Отправить изменения на GitHub с помощью Git push.
👩‍💻 Author
Name: Your Name
Course: QA Automation with Python
GitHub: https://github.com/USERNAME


