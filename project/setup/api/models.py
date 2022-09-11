from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Спилберг'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Титаник'),
    'title': fields.String(required=True, max_length=100, example='Титаник'),
    'description': fields.String(required=True, max_length=100, example='Корабль потонул...'),
    'trailer': fields.String(required=True, max_length=100, example='Айсберг'),
    'year': fields.Integer(required=True, max_length=100, example='2000'),
    'rating': fields.Float(required=True, max_length=100, example='5.0'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
    })


user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='user@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='user123'),
    'name': fields.String(required=True, max_length=100, example='Иван'),
    'surname': fields.String(required=True, max_length=100, example='Иванов'),
    'favorite_genre': fields.Nested(genre),
    })

