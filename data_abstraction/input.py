from typing import Tuple, List
from student_data import StudentData
from input_interface import InputInterface

class Input(InputInterface):
	""""This module reads and gets students data"""
	def __init__(self): super().__init__()
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def get_student_info(self) -> Tuple[List]:
		"""Overrides InputInterface.get_student_info()"""
		student_ids = [id for id in StudentData().get_data()["ID"]]
		student_names = [name for name in StudentData().get_data()["Name"]]
		student_scores = [grade for grade in StudentData().get_data()["Grade"]]
		return student_ids, student_names, student_scores