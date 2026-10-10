# MEML v6.9: Модель единого мирового листа в 6 измерениях

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23259768.svg)](https://doi.org/10.5281/zenodo.23259768)

Шестимерная модель идентичности частиц без струн, без GUT и без суперсимметрии.


## Что решает модель

Расчеты неверны

## Структура репозитория

| Папка | Содержимое |
|---|---|
| `paper/` | LaTeX-исходник и PDF статьи |
| `sterile-dm/` | Параметры и исходники sterile-dm |
| `data/` | Сырой вывод расчёта |
| `scripts/` | Python-скрипты для графиков |

## Воспроизведение

```bash
git clone https://github.com/kolbasa1972/meml-v6.9.git
cd meml-v6.9/sterile-dm
gfortran -O2 -std=legacy -fallow-argument-mismatch -o sterile-nu.exe \
    src/*.f90 src/*.f
./sterile-nu.exe params.ini > ../data/output_T_evolution.dat
```

## Ключевые предсказания

## Цитирование

```
Юров Д. В. Модель единого мирового листа (MEML) в 6 измерениях. Версия 6.9. 2026.
```

## Лицензия

- Код: MIT
- Статья: CC-BY-4.0

## Автор

- ORCID: [0009-0006-5467-7510](https://orcid.org/0009-0006-5467-7510)
