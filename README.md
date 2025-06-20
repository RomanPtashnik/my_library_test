# tests for a library that works with text data

This repository is used to test the text manipulation library

# Installation

Для установки теста необходимо клонировать проект: 
'''git clone https://github.com/RomanPtashnik/my_library_test.git'''
После установки репозитория, создайте виртуальную машину в проекте:
'''python - m venv .venv'''
Установите требования:
'''pip install -r .\requirements.txt'''
после выполнения используем команду:
'''pytest -v -s --alluredir results'''
тестирование проведенно, для получения отчёта вводим в консоль:
'''allure serve results'''




