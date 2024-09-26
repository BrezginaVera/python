"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def my_func(name, surname, dob, country, mail, phone):
    print(f"Name - {name}; Surname - {surname}; Date of birth - {dob}; Country - {country}; E-mail - {mail}; Phone - {phone}")


my_func(name='Vera', surname='Brezgina', dob='01.07.1995', country='Russia', mail='verashashkovskaya@gmail.com', phone=89851366449)
