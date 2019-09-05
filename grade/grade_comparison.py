from typing import List, Tuple

from grade.grade import Grade


def compare_grades(old_grades: List[Grade], new_grades: List[Grade]) -> List[Tuple[Grade, Grade]]:
    """
    :param old_grades: Comparison object 'old'
    :param new_grades: Comparison object 'new'
    :return: list differences between old and new grades represented by tuples (old, new) or (None, new) (if new grade)
    """
    remaining_new = list(new_grades)
    differences = []

    for old_grade in old_grades:
        try:
            new_grade = remaining_new.pop(remaining_new.index(old_grade))

            if new_grade.grade != old_grade.grade:
                differences.append((old_grade, new_grade))
        except ValueError:
            differences.append((old_grade, None))

    differences.extend(map(lambda orphan_grade: (None, orphan_grade), remaining_new))

    return differences
