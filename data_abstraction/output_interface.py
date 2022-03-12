from typing import Dict, List, Tuple

class OutputInterface:
	"""Output Interface"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()
	
	def output_grade_statistics(self, arg: Dict) -> str: pass
	def output_average_grade(self, arg: float) -> str: pass
	def output_sorted_grades(self, arg: List[Tuple]) -> str: pass