import main as app
import pytest

#Test for the connection to the postgres database
def test_connection_database():
    con , val = app.connection_database()
    assert val == 1

#Test for the creation of a task in the database
def test_create_todo():
    con , val = app.connection_database()
    app.create_todo(con, "testTodo")
    assert val == 1

#Test for the update of a task inside the database
def test_update_todo():
    con , val = app.connection_database()
    app.update_todo(con, "testTodo", "testTodoUpdate")
    assert val == 1

#Test for delete a task in the database
def test_delete_todo():
    con , val = app.connection_database()
    app.delete_todo(con, "testTodoUpdate")
    assert val == 1

#Test to read all tasks in the database
def test_get_todo():
    con , val = app.connection_database()
    app.get_todo(con)
    assert val==1