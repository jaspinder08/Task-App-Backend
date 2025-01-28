from models.task import Tasks
from models.user import User

def task_create():
    task =  Tasks(title =" my first task", content =" This is my first content",)
    assert task.title == "  my first task"
    assert task.content ==" This is my first content"


def task_user_relationship():
    user = User(
        username = "user", 
        email ="user.email@gmail.com",
        hashed_password ="password,"
    )
    task = Tasks(
        title=" my first task",
        content=" This is my first content",
        author ="user"
    )
    assert task.author == user
    assert user.tasks == [task]
