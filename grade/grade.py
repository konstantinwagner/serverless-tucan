from marshmallow import Schema, fields, post_load


class Grade:
    """
    Represents a grade (equivalence is defined by title and date)
    """

    def __init__(self, title: str, grade: float, date: str):
        self.title = title
        self.grade = grade
        self.date = date

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.title == other.title and self.date == other.date


class GradeSchema(Schema):
    """
    Represents the json grade schema for database dumps.
    """

    title = fields.Str()
    grade = fields.Number()
    date = fields.Str()

    @post_load
    def make_grade(self, data, **kwargs):
        return Grade(title=data["title"], grade=data["grade"], date=data["date"])
