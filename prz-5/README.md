# Практическое задание №5. Контроль целостности.

Выполнил Сердюков Матвей, группа ББМО-01-23

## Подготовленная ВМ с ОС Astra Linux SE 1.7

![](screenshots/01-vm-ready.png)

## Проверка работы МКЦ

![](screenshots/02-mkc-on.png)

## Создание файла, которому будет присвоена метка целостности

![](screenshots/03-create-file.png)

## Добавление метки созданному файлу

![](screenshots/04-add-metka.png)

## Попытка записи в файл в сессии с низким уровнем целостности

![](screenshots/05-access-denied.png)

## Проверка работы замкнутой программной среды

![](screenshots/06-zps-enabled.png)

## Блокировка выполнения неподписанного файла

![](screenshots/07-zps-works.png)

## Подсчёт контрольной суммы файла утилитой `gostsum`

![](screenshots/08-checksum.png)

## Инициализация `afick`

![](screenshots/09-init-afick.png)

## Отслеживание изменений в ФС с помощью `afick`

![](screenshots/10-changes.png)