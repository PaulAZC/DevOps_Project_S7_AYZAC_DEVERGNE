import main as app
import pytest

################################################################################
def test_connection_database():
    con , val = app.connection_database()
    assert val == 1

################################################################################
def test_create_table():
    con , val = app.connection_database()
    val = app.create_table(con)
    assert val == 1

################################################################################
def test_create_todo():
    con , val = app.connection_database()
    app.create_todo(con, "testTodo")
    assert val == 1

################################################################################
def test_update_todo():
    con , val = app.connection_database()
    app.update_todo(con, "testTodo", "testTodoUpdate")
    assert val == 1

################################################################################
def test_delete_todo():
    con , val = app.connection_database()
    app.delete_todo(con, "testTodoUpdate")
    assert val == 1