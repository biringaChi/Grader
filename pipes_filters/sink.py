from source import ReadData
from sort_filter import SortGrade
from grade_filter import GradeStatics

# This pipeline calculates and prints out how many students got A, B, C, D and F
pipeline_1 = GradeStatics().get_grade_statistics(ReadData().get_student_info())
print(pipeline_1)

# This pipeline calculates and prints out the average grade
pipeline_2 = GradeStatics().get_average(ReadData().get_student_info())
print(pipeline_2)

# This pipeline calculates and prints sorted out the grades, together with the corresponding students’ IDs.
pipeline_3 = SortGrade().sort_grade(ReadData().get_student_info())
print(pipeline_3)