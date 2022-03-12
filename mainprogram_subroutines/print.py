from typing import Dict, List, Tuple
from pandas.core.frame import DataFrame

class Print:
	"""This module displays to screen relevant information"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def display_student_data(self, arg: DataFrame): print(arg)

	def display_grade_statistics(self, arg: Dict) -> str:
		for grade, n_students in arg.items():
			print(f"{n_students} students got {grade}")
	
	def display_average_grade(self, arg: float) -> str: print(f"Average Grade: {arg}")

	def display_sorted_grades(self, arg: List[Tuple]) -> str:
		for sorted_data in arg:
			print(f"Grade: {sorted_data[0]}, Student ID: {sorted_data[1]}")