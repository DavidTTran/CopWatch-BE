import unittest
import json
from app import create_app, db
from app.models import Report

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

class TestReport(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.test_app = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_it_can_create_a_report(self):
        report = Report(description='test', city="Denver", state="Colorado", zip_code="80104")
        with self.app.app_context():
            db.session.add(report)
            db.session.commit()

        response = self.test_app.get(
            '/api/reports',
            follow_redirects=True
        )

        self.assertEqual(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['count'], 1)
