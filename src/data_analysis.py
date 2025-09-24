# TODO

# Read CSV and return list of student data
def load_students(filename):
    with open(filename, 'r') as file:
        content = file.readlines()[1:]
        return content

# Calculate and return average
def calculate_average_grade(students): 
    sum = 0
    for s in students:
        score = int(s.strip().split(',')[2])
        sum += score
    avg = sum/len(students)
    return avg


# Count students in Math
def count_math_students(students):
    pass

# Create formatted report string
def generate_report():
    pass

# Write report to file
def save_report(report, filename):
    pass

if __name__ == "__main__":
    print("Hi")

    contents = load_students("data/students.csv")
    print(f"File content: {contents}")

    avg = calculate_average_grade(contents)
    print(f"{avg:.1f}")

