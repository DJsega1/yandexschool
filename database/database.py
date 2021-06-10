from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, Table, MetaData, insert
from sqlalchemy import create_engine

metadata = MetaData()

engine = create_engine('postgresql+psycopg2://postgres:qwerty@localhost:5432/vita_db')

cities = Table('cities', metadata,
               Column('id', Integer(), primary_key=True, autoincrement=True),
               Column('title', VARCHAR(30), nullable=False))

users = Table('users', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('first_name', VARCHAR(30), nullable=False),
              Column('last_name', VARCHAR(40), nullable=False),
              Column('email', VARCHAR(50), nullable=False),
              Column('city_id', Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"),
                     nullable=False)
              )

conn = engine.connect()
metadata.create_all(engine)

cities_data = [
    {"title": "Саранск"},
    {"title": "Москва"},
    {"title": "Челябинск"},
    {"title": "Воронеж"}
]

users_data = [
    {
        "first_name": "Александр",
        "last_name": "Смутин",
        "email": "asd@mail.ru",
        "city_id": 3
    },
    {
        "first_name": "Мария",
        "last_name": "Волкова",
        "email": "volk@gmail.com",
        "city_id": 2
    },
    {
        "first_name": "Павел",
        "last_name": "Гришин",
        "email": "pudge@yandex.ru",
        "city_id": 1
    },
    {
        "first_name": "Яна",
        "last_name": "Вовкина",
        "email": "yana@mail.ru",
        "city_id": 4
    },
    {
        "first_name": "Елена",
        "last_name": "Исаева",
        "email": "isa@mail.ru",
        "city_id": 2
    },
    {
        "first_name": "Михаил",
        "last_name": "Пивкин",
        "email": "misha@gmail.com",
        "city_id": 2
    },
    {
        "first_name": "Георгий",
        "last_name": "Жуков",
        "email": "juke@mail.ru",
        "city_id": 3
    },
    {
        "first_name": "Анна",
        "last_name": "Казакова",
        "email": "anya@gmail.com",
        "city_id": 1
    },
    {
        "first_name": "Иван",
        "last_name": "Морозов",
        "email": "moroz@yandex.ru",
        "city_id": 2
    },
    {
        "first_name": "Станислав",
        "last_name": "Кошкин",
        "email": "stasik@mail.ru",
        "city_id": 4
    }
]

conn.execute(insert(cities), cities_data)
conn.execute(insert(users), users_data)
