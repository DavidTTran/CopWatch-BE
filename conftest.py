# import pytest
# from app import create_app
# from app.models.report import Report
#
# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')
#     testing_client = flask_app.test_client()
#     ctx = flask_app.app_context()
#
#     ctx.push()
#     yield testing_client
#     ctx.pop()
#
# @pytest.fixture(scope='module')
# def init_database():
#     db.create_all()
#
#     report1 = Report(description='Report 1', city='Denver', state='Colorado', zip_code='80104',
#                     officer_name='Deputy Harris, Officer Riley', created_date='2020-07-03 02:41',
#                     badge_number='12314142-1231', parties='Bob Barker')
#     report2 = Report(description='Report 2', city='Denver', state='Colorado', zip_code='80215',
#                     officer_name='Deputy Smith, Officer Jackson', created_date='2020-07-21 03:47',
#                     badge_number='141234142-1331', parties='Daniel Day Lewis')
#
#     db.session.add(report1)
#     db.session.add(report2)
#
#     db.session.commit()
#
#     yield db
#     db.drop_all()
#