import numpy as np
from typing import Dict
from input import ReadData
from collections import Counter

class GradeStatistics(ReadData):
	"""This module calculates the statistics of students grades"""
	def __init__(self) -> None:
		super().__init__()
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()
		
	def get_grade_statistics(self) -> Dict:
		_, _, student_scores = self.get_student_info()
		letter_grades = []
		for score in student_scores:
			if score in range(90, 1001): letter_grades.append("A")
			elif score in range(80, 90): letter_grades.append("B")
			elif score in range(70, 80): letter_grades.append("C")
			elif score in range(60, 70): letter_grades.append("D")
			else: letter_grades.append("F")
		return Counter(letter_grades)
		
	def get_average(self) -> float:
		_, _, student_scores = self.get_student_info()
		return np.mean(student_scores)