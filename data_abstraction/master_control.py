from output import Output
from sortgrade import SortGrade
from gradestatistics import GradeStatistics

def main():
	"""Main Progam"""
	Output().output_grade_statistics(GradeStatistics().get_grade_statistics())
	Output().output_average_grade(GradeStatistics().get_average())
	Output().output_sorted_grades(SortGrade().sort_grade())

if __name__ == "__main__":
	main()