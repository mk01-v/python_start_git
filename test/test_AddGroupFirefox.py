# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password ="secret")
    app.group.create(Group(name="group_name_cool", header="group_header_cool_logo"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password ="secret")
    app.group.create(Group(name="", header=""))
    app.session.logout()

def test_delete_first_group(app):
    app.session.login(username ="admin", password ="secret")
    app.group.delete_first_group()
    app.session.logout()