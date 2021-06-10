from sqlalchemy import Column, ForeignKey, Integer, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2 =//postgres =qwerty@localhost =5432/vita_db')
session = Session(bind=engine)
Base = declarative_base()


class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(100), nullable=False)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(100), nullable=False)
    first_name = Column(VARCHAR(30), nullable=False)
    last_name = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)


data = [
    Cities(title="Саранск"),
    Cities(title="Москва"),
    Cities(title="Челябинск"),
    Cities(title="Воронеж"),
    Users(first_name="Александр", last_name="Смутин", email="asd@mail.ru", cities_id=3),
    Users(first_name="Мария", last_name="Волкова", email="volk@gmail.com", cities_id=2),
    Users(first_name="Павел", last_name="Гришин", email="pudge@yandex.ru", cities_id=1),
    Users(first_name="Яна", last_name="Вовкина", email="yana@mail.ru", cities_id=4),
    Users(first_name="Елена", last_name="Исаева", email="isa@mail.ru", cities_id=2),
    Users(first_name="Михаил", last_name="Пивкин", email="misha@gmail.com", cities_id=2),
    Users(first_name="Георгий", last_name="Жуков", email="juke@mail.ru", cities_id=3),
    Users(first_name="Анна", last_name="Казакова", email="anya@gmail.com", cities_id=1),
    Users(first_name="Иван", last_name="Морозов", email="moroz@yandex.ru", cities_id=2),
    Users(first_name="Станислав", last_name="Кошкин", email="stasik@mail.ru", cities_id=4)
]

session.add_all(data)
session.commit()
session.close()
