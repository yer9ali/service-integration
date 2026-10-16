# service-integration

Плагин Claude Code: проводит интеграцию вашего репозитория с нашим сервисом по документации
этого сервиса. Скилл находит `docs/integration` и `reference/openapi.json` нужного сервиса,
определяет вашу роль (например, кассовое ПО или интегратор), строит план по чеклисту
готовности, пишет клиент и тесты в стиле вашего репозитория и в конце выдаёт, что осталось и
какие вопросы задать команде сервиса.

## Установка

```
/plugin marketplace add https://github.com/yer9ali/service-integration.git
/plugin install service-integration@service-integration
```

Обновление: `/plugin update service-integration@service-integration`.

## Вызов

Из корня репозитория, который интегрируется:

- `/service-integration ofd` — интеграция с ОФД Metrix, роль скилл спросит или определит сам;
- `/service-integration ofd касса` — сразу с ролью;
- `/service-integration ../fdo_api` — по локальному клону сервиса;
- `/service-integration <git-URL>` — сервис, которого нет в реестре.

При конфликте имён используйте `/service-integration:service-integration`.

## Какие сервисы поддерживаются

Реестр — `plugins/service-integration/skills/service-integration/reference/services.json`.

| Имя | Сервис |
|---|---|
| `ofd` | ОФД Metrix (fdo_api) |

Нужен доступ на чтение к репозиторию сервиса: скилл читает документацию оттуда.

## Как подключить свой сервис

1. Оформите `docs/integration` по каркасу —
   `plugins/service-integration/skills/service-integration/reference/docs-contract.md`.
   Образец — `docs/integration` в fdo_api.
2. Добавьте сервис в `services.json` и поднимите версию плагина в `plugin.json`.

## Что скилл не делает

- Не просит и не хранит секреты: ключи выставляются переменными окружения.
- Не коммитит и не пушит без просьбы.
- Не придумывает ручки: всё, чего нет в документации сервиса, попадает в итог как вопрос к
  его команде.
