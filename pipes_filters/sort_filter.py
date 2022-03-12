from source import ReadData
from typing import Dict, List, Tuple

class SortGrade(ReadData):
	"""This module sorts grades together with the corresponding students IDs"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def sort_grade(self, student_info: Tuple[List]) -> Dict:
		student_ids, _, student_scores = student_info
		return sorted({score : id for score, id in zip(student_scores, student_ids)}.items(), reverse=True)