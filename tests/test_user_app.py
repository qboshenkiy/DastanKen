from user_app.user import User
from user_app.main import add_user, list_users, find_user, users  # Добавим users из main

def test_add_user():
    users.clear()  # Очистим список перед каждым тестом
    add_user("test_user", "test@example.com")
    assert len(users) == 1

def test_list_users(capsys):
    users.clear()
    users.append(User("test_user", "test@example.com"))
    list_users()
    captured = capsys.readouterr()
    assert "test_user" in captured.out

def test_find_user(capsys):
    users.clear()
    users.append(User("test_user", "test@example.com"))
    find_user("test_user")
    captured = capsys.readouterr()
    assert "User found" in captured.out

    find_user("unknown_user")
    captured = capsys.readouterr()
    assert "No user found" in captured.out
