import json

from tucan_tools.grades_exporter import get_grades
from tucan_tools.helper import get_user_credentials

from grade import grade_store, grade_comparison, grade_mailer
from grade.grade import Grade


# Default handler called regularly to compare grades
def fetch_grades(event, context):
    new_grades = list(map(lambda raw: Grade(raw["title"], raw["grade"], raw["date"]), get_grades(False)))
    old_grades = grade_store.fetch_and_update_grades(get_user_credentials()["username"], new_grades)

    grade_changes = grade_comparison.compare_grades(old_grades, new_grades)

    # Only send mail for changes
    if len(grade_changes) > 0:
        grade_mailer.send_grade_mail(grade_changes)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
