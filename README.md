# Скрипт для редактирования данных в электронном дневнике

Предназначен для внесения изменений в базу данных (БД) электронного дневника школы.
Позволяет изменять оценки одного ученика, удалять данные о замечаниях учителей и добавлять запись о похвале на последнем уроке по выбранному случайно или определенному предмету.

## Окружение

### Зависимости

- [Установите](https://habr.com/ru/articles/822557/) Python3 и среду разработки
- Скачайте репозиторий [электронного дневника школы](https://github.com/devmanorg/e-diary).
- Скачайте [базу данных](https://dvmn.org/filer/canonical/1562234129/166/) и расположите ее в репозитории рядом с файлом `manage.py`
- Ознакомьтесь с [README](https://github.com/devmanorg/e-diary/blob/master/README.md) электронного дневника
- В корневой папке репозитория создайте `.env` файл, содержащий часть настроек проекта в виде переменных окружения. [Подробности](https://github.com/devmanorg/e-diary/blob/master/README.md#переменные-окружения)
- Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```pycon
pip install -r requirements.txt
```
- **ВАЖНО: при работе с Python версии 3.12 и выше необходимо установить библиотеку setuptools**:
```pycon
pip install setuptools==75.3.0
```

## Запуск

- Откройте `Script.py` в среде разработки или в любом текстовом редакторе
- В скрипте (см. `main()`) используется переменная `your_name`(*str*) - имя ученика, данные которого нужно изменить. 
Установите значение переменной следующим образом:
```python
your_name = 'Фамилия Имя Отчество'
```
Отчество нужно указать в том случае, если в БД имеется несколько учеников с одинаковыми фамилией и именем.
По умолчанию `your_name` содержит значение `'Фролов Иван'`
- Также в скрипте (см. `main()`) используется переменная `lesson`(*str*) - название урока, для которого нужно внести запись о похвале.
По умолчанию значение `lesson` выбирается случайным образом из списка `LESSONS`:
```python
lesson = random.choice(LESSONS)
```
Если необхолимо получить запись о похвале на конкретном уроке, замените содержимое переменной `lesson` следующим образом:
```python
lesson = 'Краеведение'
```
Для исключения ошибок в работе скрипта рекомендуется копировать название урока непосредственно из списка `LESSONS`
- Список `PRAISES` содержит фразы, случайным образом попадающие в запись о похвале на уроке. По умолчанию в `PRAISES` находятся фразы-заглушки, использованные исключительно для написания и отладки кода.
Измените `PRAISES` и/или дополните его [строковым](https://pythonexamples.org/python-list-of-strings/) содержимым по вашему усмотрению.
- Создайте БД командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`
- Создайте новое окно терминала (Ctrl+Shift+P в VSCode, Ctrl+Shift+`(обратная кавычка) в PyCharm)
- Зайдите в Shell:
```pycon
python3 manage.py shell
```
- Скопируйте в Shell код скрипта, но пока что не запускайте и не сохраняйте.
- По умолчанию скрипт запускает три функции: `fix_marks` - исправляет оценки в БД за все время, `fix_chastisements` - удаляет замечания из БД за все время, `create_commendation` - создает запись со случайной похвалой (из списка `PRAISES`) на **последнем** уроке по предмету заданному в `lesson`.
- Удалите из скопированного в Shell кода строки с функциями, не требуемыми в настоящий момент.
- Сохраните код в Shell (Поместить курсор в конец кода, после чего дважды нажать Enter)
- Запустить выполнение скрипта в Shell:
```
main()
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
