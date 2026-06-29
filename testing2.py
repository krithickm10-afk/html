
grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Evan": 64
}

total_score = 0
for score in grade_book.values():
    total_score += score

class_average = total_score / len(grade_book)
print("Class Average: {class_average:}")

top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)

print(f"Top Scorer: {top_student} ({grade_book[top_student]})")
print(f"Bottom Scorer: {bottom_student} ({grade_book[bottom_student]})")
print("-" * 35)


search_name = input("Enter the student's name to look up their grade: ").strip()

grade = grade_book.get(search_name, "Student not found in the grade book.")

print("Result: {grade}")