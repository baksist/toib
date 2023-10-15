# Лабораторная работа №1

## Развёртывание Keycloak с использованием Docker

![](screenshots/keycloak-docker.png)

![](screenshots/start-keycloak.png)

![](screenshots/it-works.png)

## Открытие веб-интерфейса администрирования Keycloak

![](screenshots/open-web.png)

![](screenshots/login-keycloak.png)

## Создание собственного realm

![](screenshots/create-realm.png)

## Создание пользователей `appadmin` и `user`

![](screenshots/create-appadmin.png)

![](screenshots/create-user.png)

![](screenshots/created-users.png)

## Развёртывание приложения Grafana с использованием Docker

![](screenshots/grafana-docker-compose.png)

![](screenshots/start-grafana.png)

## Создание клиента в Keycloak

![](screenshots/create-client.png)

![](screenshots/client-configure.png)

![](screenshots/client-urls.png)

## Создание ролей `admin` и `viewer` для их сопоставления в Grafana

![](screenshots/grafana-roles.png)

## Назначение созданным пользователям ролей в Grafana

![](screenshots/add-role-1.png)

![](screenshots/add-role-2.png)

## Настройка добавления текущей роли пользователя в аутентификационный токен

![](screenshots/add-mapper.png)

## Настройка аутентификации через Keycloak в Grafana

![](screenshots/grafana-config.png)

## Возможность аутентифицироваться через Keycloak на странице входа

![](screenshots/grafana-oauth-enabled.png)

## Успешный вход и применение ролей у пользователя `appadmin`

![](screenshots/login-page.png)

![](screenshots/auth-success.png)

![](screenshots/role-success.png)

## Успешный вход и применение ролей у пользователя `user`

![](screenshots/auth-success-2.png)

![](screenshots/role-success-2.png)

## Включение двухфакторной аутентификации в Keycloak

![](screenshots/enable-otp.png)

## Страница настройки 2FA при попытке аутентифицироваться

![](screenshots/setup-otp.png)

## Страница ввода одноразового кода при входе в аккаунт

![](screenshots/otp-enabled.png)