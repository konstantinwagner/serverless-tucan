import os
from typing import List

import boto3

from grade.grade import Grade, GradeSchema

db_table = boto3.resource("dynamodb").Table(os.environ["GRADES_TABLE"])


def fetch_and_update_grades(user_id: str, new_grades: List[Grade]) -> List[Grade]:
    """
    Updates the grades stored in database with the given values and returns previously stored grades.
    :param user_id: key under which the grades are stored inside the db
    :param new_grades: list of grades to dump into the database (will replace existing)
    :return: previously stored grades
    """
    response = db_table.update_item(
        Key={
            "userId": user_id
        },
        AttributeUpdates={
            "grades": {
                "Value": GradeSchema(many=True).dumps(new_grades),
                "Action": "PUT"
            }
        },
        ReturnValues="ALL_OLD"
    )
    old_grades = GradeSchema(many=True).loads(response["Attributes"]["grades"]) if "Attributes" in response else []

    return old_grades
