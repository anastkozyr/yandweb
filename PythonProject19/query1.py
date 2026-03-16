from flask import Flask

from data.jobs import Jobs
from data.users import User

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(input())
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.address == "module_1"):
        print(user.name)

if __name__ == '__main__':
    main()


def main():
    global_init(input())

    db_sess = create_session()

    for user in db_sess.query(User).filter(User.address == "module_1",
                                           User.speciality.notlike("%engineer%"),
                                           User.position.notlike("%engineer%")):
        print(user.id)


    if __name__ == '__main__':
        main()

