import json
import os
from typing import List, Tuple

import boto3

from grade.grade import Grade

ses = boto3.client("ses")
recipient = os.environ["RECIPIENT_MAIL_ADDRESS"]
sender = os.environ["SENDER_MAIL_ADDRESS"]


def send_grade_mail(grade_changes: List[Tuple[Grade, Grade]]):
    """
    Send an notification email to user which contains all given grade changes.
    :param grade_changes: grade changes to notify about
    """
    ses.send_templated_email(
        Source=sender,
        Destination={
            "ToAddresses": [
                recipient
            ]
        },
        Template=os.environ["NEW_GRADES_TEMPLATE"],
        TemplateData=json.dumps({
            "gradeChanges": list(map(lambda change: {
                "title": change[0].title if change[0] is not None else change[1].title,
                "oldGrade": str(change[0].grade) if change[0] is not None else "-",
                "newGrade": str(change[1].grade) if change[1] is not None else "-"
            }, grade_changes))
        })
    )
