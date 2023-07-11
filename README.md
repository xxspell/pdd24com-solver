# pdd24.com solver

Автоматическое решение внутреннего экзамена ПДД на http://www.pdd24.com/for-school

## Клонирование репозитория

Чтобы клонировать репозиторий, выполните следующие команды:

```bash
git clone https://github.com/xxspell/pdd24com-solver.git
cd pdd24com-solver
```

## Установка виртуального окружения (venv)

Для создания и активации виртуального окружения (venv) выполните следующие команды:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Установка зависимостей

Для установки зависимостей выполните команду:

```bash
pip install -r requirements.txt
```
## Конфигурация приложения

Для настройки приложения, отредактируйте файл _.env_
```bash
# Фамилия
LASTNAME="Фам"

# Имя
FIRSTNAME="Имя"

# Отчество
MIDDLENAME="Отч"

# Почта учителя
EMAILTEACHER="email@email.com"
```

## Запуск проекта
```bash
python main.py
```