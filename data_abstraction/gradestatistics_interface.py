from typing import Dict

class GradeStatisticsInterface:
	"""Grade Statistics Interface"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()
		
	def get_grade_statistics(self) -> Dict:
		pass
		
	def get_average(self) -> float:
		pass