from typing import Dict, List, Tuple
from output_interface import OutputInterface

class Output(OutputInterface):
	"""This module outputs to screen relevant information"""
	def __init__(self): super().__init__()
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def output_grade_statistics(self, arg: Dict) -> str:
		"""Overrides OutputInterface.output_grade_statistics()"""
		for grade, n_students in arg.items():
			print(f"{n_students} students got {grade}")
	
	def outputs_average_grade(self, arg: float) -> str:
		"""Overrides OutputInterface.output_average_grade()"""
		print(f"Average Grade: {arg}")

	def output_sorted_grades(self, arg: List[Tuple]) -> str:
		"""Overrides OutputInterface.output_sorted_grades()"""
		for sorted_data in arg:
			print(f"Grade: {sorted_data[0]}, Student ID: {sorted_data[1]}")