# TODO

# Read CSV and return list of student data
def load_students(filename:str):
    with open(filename, 'r') as file:
        content = file.readlines()[1:]

    # Initialized an empty list to store student data
    students = []

    # Iterate through list "content" and split each element. 
    # Store each student data in a dictionary and append into the students list
    for s in content:
        temp = s.strip().split(',')
        students.append({"name": temp[0], "age": int(temp[1]), "grade": int(temp[2]), "subject": temp[3]})
        
    return students

# Calculate and return average
def calculate_average_grade(students:list[dict]): 
    sum = 0

    #iterate through student to get their score and add to sum
    for s in students:
        sum += s["grade"]

    # divide sum with number of student to get average
    avg = sum/len(students)

    return avg


# Count students in Math
def count_math_students(students:list[dict]):
    count = 0
    for s in students:
        if s["subject"] == "Math":
            count += 1

    return count


# Create formatted report string
def generate_report(total:int, average:float, math_count:int):
    report = ["Basic Analysis Results:"]
    report.append(f"- Number of student: {total}")
    report.append(f"- Class average: {average:.1f}")
    report.append(f"- Number of Math student: {math_count}")
    return report

# Write report to file
def save_report(report:list[str], filename:str):
    with open(filename, 'w') as file:
        for r in report:
            file.write(f"{r}\n")


# Perform the analysis
def main():
    contents = load_students("data/students.csv")
    # print(contents)
    avg = calculate_average_grade(contents)
    math_count = count_math_students(contents)
    total = len(contents)
    report = generate_report(total, avg, math_count)
    save_report(report, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
