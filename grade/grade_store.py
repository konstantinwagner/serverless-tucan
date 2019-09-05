import os
from typing import List, Optional

import boto3

from grade.grade import Grade, GradeSchema

db_table = boto3.resource("dynamodb").Table(os.environ["GRADES_TABLE"])


def fetch_and_update_grades(user_id: str, grades: List[Grade]) -> List[Grade]:
    new_grades = GradeSchema(many=True).dumps(grades)

    response = db_table.update_item(
        Key={
            "userId": user_id
        },
        AttributeUpdates={
            "grades": {
                "Value": new_grades,
                "Action": "PUT"
            }
        },
        ReturnValues="ALL_OLD"
    )
    old_grades = GradeSchema(many=True).loads(response["Attributes"]["grades"]) if "Attributes" in response else []

    return old_grades
