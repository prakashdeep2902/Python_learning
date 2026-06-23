MathMarks = int(input("Enter the Math Marks: "))
ScienceMarks = int(input("Enter the Science Marks: "))
EnglishMarks = int(input("Enter the English Marks: "))

TotalMarks = MathMarks + ScienceMarks + EnglishMarks

Per_TotalMarks = round((TotalMarks / 300) * 100)

print("Percentage:", Per_TotalMarks)

Total_pass_P = 40
Pass_Mark_each = 33

if (
    MathMarks >= Pass_Mark_each
    and ScienceMarks >= Pass_Mark_each
    and EnglishMarks >= Pass_Mark_each
    and Per_TotalMarks >= Total_pass_P
):
    print("Result: Pass")
else:
    print("Result: Fail")
