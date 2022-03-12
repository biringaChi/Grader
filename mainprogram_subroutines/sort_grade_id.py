from typing import Dict
from input import ReadData

class SortGrade(ReadData):
	"""This module sorts grades together with the corresponding students IDs"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def sort_grade(self) -> Dict:
		student_ids, _, student_scores = self.get_student_info()
		return sorted({score : id for score, id in zip(student_scores, student_ids)}.items(), reverse=True)