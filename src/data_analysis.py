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
    count = 0
    for s in students:
        subject = s.strip().split(',')[3]
        if subject == "Math":
            count += 1
    return count


# Create formatted report string
def generate_report(average, math_count):
    print(f"Class average: {average:.1f}")
    print(f"Number of Math student: {math_count}")

# Write report to file
def save_report(report, filename):
    pass

def main():
    contents = load_students("data/students.csv")
    # print(f"File content: {contents}")
    avg = calculate_average_grade(contents)
    math_count = count_math_students(contents)
    generate_report(avg, math_count)
    save_report(report, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
