#!/bin/bash

echo "wait..."
sleep 5  

echo "Запуск Unit-тестов..."
pytest --html=report.html --self-contained-html

echo "Тестирование завершено! Отчет доступен в report.html"
