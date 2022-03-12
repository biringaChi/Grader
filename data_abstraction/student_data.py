import pandas as pd 
from pandas.core.frame import DataFrame

class StudentData:
	def __init__(self, data = "students.csv") -> None: self.__data = data
	def __str__(self) -> str: return self.__class__.__name__
	def __repr__(self) -> str: return self.__str__()

	def set_data(self, data: str) -> None: self.__data = data
	def get_data(self) -> DataFrame: return pd.read_csv(self.__data)