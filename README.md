# Описание
secure-pipeline — это пример безопасного CI/CD pipeline с интеграцией SAST (Static Application Security Testing) на базе Bandit, работающий на GitHub-hosted runners.
Проект включает:
	•	Уязвимый тестовый код для демонстрации обнаружения уязвимостей.
	•	Проверку кода на SQL Injection, hardcoded secrets и unsafe deserialization.
	•	Автоматическую сборку Docker-контейнера и его деплой.
	•	Security Gate, который блокирует коммиты с HIGH/важными уязвимостями.
