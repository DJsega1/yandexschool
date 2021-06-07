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
              Column('cities_id', Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"),
                     nullable=False)
              )

conn = engine.connect()
metadata.create_all(engine)


def execu(q):
    conn.execute(q)


execu(insert(cities).values(title="Саранск"))
execu(insert(cities).values(title="Москва"))
execu(insert(cities).values(title="Челябинск"))
execu(insert(cities).values(title="Воронеж"))
execu(insert(users).values(first_name="Александр", last_name="Смутин", email="asd@mail.ru", cities_id=3))
execu(insert(users).values(first_name="Мария", last_name="Волкова", email="volk@gmail.com", cities_id=2))
execu(insert(users).values(first_name="Павел", last_name="Гришин", email="pudge@yandex.ru", cities_id=1))
execu(insert(users).values(first_name="Яна", last_name="Вовкина", email="yana@mail.ru", cities_id=4))
execu(insert(users).values(first_name="Елена", last_name="Исаева", email="isa@mail.ru", cities_id=2))
execu(insert(users).values(first_name="Михаил", last_name="Пивкин", email="misha@gmail.com", cities_id=2))
execu(insert(users).values(first_name="Георгий", last_name="Жуков", email="juke@mail.ru", cities_id=3))
execu(insert(users).values(first_name="Анна", last_name="Казакова", email="anya@gmail.com", cities_id=1))
execu(insert(users).values(first_name="Иван", last_name="Морозов", email="moroz@yandex.ru", cities_id=2))
execu(insert(users).values(first_name="Станислав", last_name="Кошкин", email="stasik@mail.ru", cities_id=4))

conn.close()