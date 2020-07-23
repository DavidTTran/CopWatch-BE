from app.models.report import Report

def test_new_report():
    report = Report('Report 1', 'Denver', 'Colorado', '80104',
                    'Deputy Harris, Officer Riley', '2020-07-03 02:41',
                    '12314142-1231', 'Bob Barker')
    
    assert report.description == 'Report 1'
    assert report.city == 'Denver'
    assert report.state == 'Colorado'
    assert report.zip_code == '80104'
    assert report.officer_name == 'Deputy Harris, Officer Riley'
    assert report.created_date == '2020-07-03 02:41'
    assert report.badge_number == '12314142-1231'
    assert report.parties == 'Bob Barker'
