# TODO

# Read CSV and return list of student data
def load_students(filename):
    with open(filename, 'r') as file:
        content = file.readlines()[1:]
        return content

# Calculate and return average
def calculate_average_grade(students): 
    sum = 0

    #iterate through student to get their score and add to sum
    for s in students:
        score = int(s.strip().split(',')[2])
        sum += score

    # divide sum with number of student to get average
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
def generate_report(total, average, math_count):
    report = ["This is a basic analysis report for the class:"]
    report.append(f"- Number of student: {total}")
    report.append(f"- Class average: {average:.1f}")
    report.append(f"- Number of Math student: {math_count}")
    return report

# Write report to file
def save_report(report, filename):
    with open(filename, 'w') as file:
        for r in report:
            file.write(f"{r}\n")



def main():
    contents = load_students("data/students.csv")
    # print(f"File content: {contents}")
    avg = calculate_average_grade(contents)
    math_count = count_math_students(contents)
    total = len(contents)
    report = generate_report(total, avg, math_count)
    save_report(report, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
