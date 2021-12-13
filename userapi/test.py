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
def test_create_user():
    con , val = app.connection_database()
    app.create_user(con, "testUser", "testPassword")
    assert val == 1