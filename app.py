from datetime import date
from sqlite3 import Date
from flask import Flask, request, jasonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.postgres_ext import ArrayField

db = PostgresqlDatabase('ms', user='leontzuchiangchan',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Title(BaseModel):
    name = CharField()
    year = IntegerField()
    mobile_suit = ArrayField(CharField)
    protagonist = CharField()


db.connect()
db.drop_tables([Title])
db.create_tables([Title])
