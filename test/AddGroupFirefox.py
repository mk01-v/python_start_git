# -*- coding: utf-8 -*-
from fixture.application import application
import pytest
from model.group import Group

@pytest.fixture()
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username ="admin", password ="secret")
    app.group.create(Group(name="group_name_cool", header="group_header_cool_logo"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username ="admin", password ="secret")
    app.group.create(Group(name="", header=""))
    app.session.logout()

