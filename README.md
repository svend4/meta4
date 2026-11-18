# meta4 — Flower Shop Project

Репозиторий алгоритмической задачи оптимизации букета цветов по бюджету («Магазин цветов» / *Flower Shop Project*).

> [!NOTE]
> В ветке `main` в настоящее время находятся только файл лицензии `LICENSE` и этот `README.md`. Исходный код решателя на Python размещён в неслитой ветке [`copilot/flower-shop-setup`](../../tree/copilot/flower-shop-setup).

## Функциональность и структура (ветка `copilot/flower-shop-setup`)

- `main.py` — консольный скрипт на чистом Python (стандартная библиотека: `collections.Counter`, `sys`), решающий серию из `t` тестовых наборов:
  - для каждого набора считываются количество доступных цветов `n`, бюджет `m` и массив значений лепестков `flowers`;
  - алгоритм перебирает уникальные номиналы `petals` и комбинирует цветы с `petals` и `petals + 1` лепестками, вычисляя максимальное суммарное число лепестков в пределах бюджета `m`.
- `.gitignore` — правила исключения кэша Python.

## Стек и запуск

- **Язык:** Python 3 (без внешних зависимостей, только `stdlib`).

```bash
# Запуск решателя с передачей входных данных через stdin (из ветки copilot/flower-shop-setup)
python3 main.py < input.txt
```

## Ветки репозитория

- `copilot/flower-shop-setup` ([PR #2](../../pull/2), draft — *«Add Python solver for «Магазин цветов» bouquet optimization»*) — содержит реализацию `main.py` и `.gitignore`.
- `copilot/fix-typo-in-documentation` ([PR #1](../../pull/1), draft — *«Update README content to match required “Hallo” text»*) — тестовое изменение `README.md` (`# meta4 / Hallo`).
- `codex/readme-overview-20261118` ([PR #3](../../pull/3), draft — *«Add concise project README»*) — шаблонная заготовка `README.md` (`# Flower Shop Project`).

## Лицензия

Проект распространяется под лицензией **GNU Affero General Public License v3.0** — см. [LICENSE](LICENSE).
