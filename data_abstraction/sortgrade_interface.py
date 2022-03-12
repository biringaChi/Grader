from typing import Dict

class SortGradeInterface:
	"""Sort Grade Interface"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def sort_grade(self) -> Dict: pass