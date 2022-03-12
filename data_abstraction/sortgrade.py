from input import Input
from typing import Dict
from sortgrade_interface import SortGradeInterface

class SortGrade(SortGradeInterface):
	"""This module sorts grades together with the corresponding students IDs"""
	def __init__(self): super().__init__()
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def sort_grade(self) -> Dict:
		"""Overrides SortGradeInterface.sort_grade()"""
		student_ids, _, student_scores = Input().get_student_info()
		return sorted({score : id for score, id in zip(student_scores, student_ids)}.items(), reverse=True)