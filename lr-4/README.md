# Лабораторная работа №4. Настройка и применение криптографических протоколов

Выполнил Сердюков Матвей, ББМО-01-23

## Создание ключевой пары GPG

![](./screenshots/01-create-key.png)
![](./screenshots/02-create-key.png)

## Просмотр созданных ключей, подписей, отпечатков

![](./screenshots/03-list.png)

## Создание отзывающего сертификата

Вывод сертификата в `stdout`:

![](./screenshots/04-revoke-stdout.png)

Запись сертификата в файл: 

![](./screenshots/05-revoke-file.png)

## Экспорт публичного ключа в бинарном и текстовом виде

![](./screenshots/06-export.png)
![](./screenshots/07-cat-binary.png)
![](./screenshots/08-cat-ascii.png)

## Создание файла для подписи

![](./screenshots/09-create-file.png)

## Создание цифровой подписи в бинарном виде

![](./screenshots/10-sign.png)

## Проверка подписи

![](./screenshots/11-verify.png)

## Создание цифровой подписи в формате ASCII

![](./screenshots/12-sign-armor.png)

## Создание цифровой подписи, вставленной в содержимое файла

![](./screenshots/13-clearsign.png)
