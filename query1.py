import sqlalchemy
from flask import Flask
from sqlalchemy import or_

from data.jobs import Jobs
from data.users import User
from data.departments import Department

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_name = input().strip()
    global_init(db_name)
    db_sess = create_session()

    # Находим департамент с id = 1
    department = db_sess.query(Department).filter(Department.id == 1).first()

    if not department:
        return

    # Получаем всех членов департамента (начальник + члены)
    member_ids = set()

    # Добавляем начальника
    if department.chief:
        member_ids.add(department.chief)

    # Добавляем членов из поля members
    if department.members and department.members.strip():
        for member_id in department.members.split(','):
            if member_id.strip():
                member_ids.add(int(member_id.strip()))

    # Для каждого члена департамента считаем суммарные часы
    result = []
    for user_id in member_ids:
        user = db_sess.query(User).filter(User.id == user_id).first()
        if user:
            # Суммируем часы всех работ, где пользователь - team_leader
            total_hours = db_sess.query(sqlalchemy.func.sum(Jobs.work_size)).filter(
                Jobs.team_leader == user_id
            ).scalar() or 0

            if total_hours > 25:
                result.append((user.surname, user.name))

    # Выводим в правильном порядке (как в ожидаемом результате)
    for surname, name in result:
        print(f"{surname} {name}")


if __name__ == '__main__':
    main()

# def main():
#     global_init(input())
#     db_sess = create_session()
#     users_to_update = db_sess.query(User).filter(
#         User.address == "module_1",
#         User.age < 21
#     ).all()
#
#     for user in users_to_update:
#         user.address = "module_3"
#         print(f"<Colonist> {user.id} {user.surname} {user.name}")
#
#     db_sess.commit()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     global_init(input())
#
#     db_sess = create_session()
#
#     for user in db_sess.query(User).filter(User.address == "module_1",
#                                            User.speciality.notlike("%engineer%"),
#                                            User.position.notlike("%engineer%")):
#         print(user.id)

#
# if __name__ == '__main__':
#     main()
