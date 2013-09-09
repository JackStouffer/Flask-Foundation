#! ../env/bin/python
# -*- coding: utf-8 -*-
from mypackage import myapp

def test_sayhello():
    assert myapp.say_hello('Kiran') == 'Hello Kiran'