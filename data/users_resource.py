from flask_restful import reqparse, abort, Api, Resource
from data import db_session, jobs_api
from data.jobs import Jobs
from flask import jsonify

from data.parser_user import parser
from data.users import User


def abort_if_user_not_found(news_id):
    session = db_session.create_session()
    users = session.query(User).get(id)
    if not users:
        abort(404, message=f"Users {id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'user': users.to_dict(
            ('name', 'surname', 'age', 'address',
             'email', 'position', 'speciality',
             'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):

    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users':
                            [item.to_dict(only=('name', 'surname', 'age', 'address',
                                                'email', 'position', 'speciality',
                                                'hashed_password')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            address=args['address'],
            email=args['email'],
            position=args['position'],
            speciality=args['speciality'],
            hashed_password=set_password(args['hashed_password'])
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})