import main as app
import pytest

#Test to upload on github
def test_connection_database():
    con , val = app.connection_database()