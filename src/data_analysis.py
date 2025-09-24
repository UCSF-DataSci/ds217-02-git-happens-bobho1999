# TODO

# Read CSV and return list of student data
def load_students(filename):
    with open(filename, 'r') as file:
        content = file.readlines()[1:]
        print(f"File content: {content}")

# Calculate and return average
def calculate_average_grade(students): 
    pass

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
    load_students("data/students.csv")
