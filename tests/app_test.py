import unittest
import json
from flask import request

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
