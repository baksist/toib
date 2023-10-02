# Остальные варианты

[Вариант 2](./other-variants/v2-password_generator.py) — Напишите программу на Python, которая определяет функцию для генерации случайных паролей указанной длины. Функция принимает необязательный параметр `length`, который по умолчанию равен 8. Если длина не указана пользователем, пароль будет состоять из 8 символов.

[Вариант 3](./other-variants/v3-password_policy_check.py) — Напишите программу на Python, чтобы проверить, соответствует ли пароль следующим критериям: длина не менее 8 символов и содержит как минимум одну прописную букву, одну строчную букву, одну цифру и один специальный символ (`!`, `@`, `#`, `$`, `%` или `&`). Если пароль соответствует критериям, выведите в консоль сообщение «Действительный пароль». Если он не соответствует критериям, напечатайте сообщение «Пароль не соответствует требованиям».

[Вариант 4](./other-variants/v4-password_policy_check_file.py) — Напишите программу на Python, которая считывает файл, содержащий список паролей, по одному в строке. Он проверяет каждый пароль на предмет соответствия определенным требованиям (например, не менее 8 символов, содержит как прописные, так и строчные буквы, а также хотя бы одну цифру и один специальный символ). Пароли, соответствующие требованиям, должны быть распечатаны программой. (`import re`)

[Вариант 5](./other-variants/v5-check_haveibeenpwned.py) — Напишите программу на Python, которая считывает файл, содержащий список имен пользователей и паролей, по одной паре в строке (через запятую). Он проверяет каждый пароль на предмет утечки данных в результате утечки данных. Вы можете использовать [API «Have I Been Pwned»](https://haveibeenpwned.com/API/v3), чтобы проверить, не была ли утечка пароля. (`import requests, hashlib`)

[Вариант 6](./other-variants/v6-bruteforcer.py) — Напишите программу на Python, которая имитирует атаку пароля методом перебора, перебирая все возможные комбинации символов. (`import string, itertools`)