# Test task for papazaim
<h2> Структура проекта: </h2>

[core](core) - логика и реализация задачи

[config](config) - класс настроек, синхронизируется с значениями переменных окружения

[database](database) - утилиты для работы с БД, entity (узел) (сущность, используемая только в рамках запросов)

[models](models) - базовая модель, модель узла и enum, используемые в рамках приложения

[migrations](migrations) - миграции, кастомный env.py файл для генерации автоматических миграций

[test](test) - асинхронные тесты

[utils](utils) - утилиты для приложения, механизм сидирования базы

[main.py](main.py) - entrypoint приложения


<h2> TODO: </h2>

- Покрыть тестами больший объем функциональности
- Асинхронное сидирование (:D)
- Рекурсивная функция сидирования для гибкости
- Dockerfile или docker-compose
