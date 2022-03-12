import pandas as pd
from typing import List, Tuple
from typing import List, Tuple
from pandas.core.frame import DataFrame

class ReadData:
	"""This module reads and gets students data"""
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()
	
	def get_data(self) -> DataFrame:
		try:
			students = pd.read_csv("students.csv")
		except FileNotFoundError as e:
			raise(e)
		return students

	def get_student_info(self) -> Tuple[List]:
		"""This method reads in student ID, names and grades"""
		student_ids = [id for id in self.get_data()["ID"]]
		student_names = [name for name in self.get_data()["Name"]]
		student_scores = [grade for grade in self.get_data()["Grade"]]
		return student_ids, student_names, student_scores