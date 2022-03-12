from print import Print
from input import ReadData
from sort_grade_id import SortGrade
from grade_statistics import GradeStatistics

def main():
	"""Main Progam"""
	Print().display_student_data(ReadData().get_data())
	Print().display_grade_statistics(GradeStatistics().get_grade_statistics())
	Print().display_average_grade(GradeStatistics().get_average())
	Print().display_sorted_grades(SortGrade().sort_grade())

if __name__ == "__main__":
	main()