# TODO

# Generic loader that checks file extension
def load_data(filename:str): 
    # Check for
    if filename.endswith(".csv"):
        print("Processing csv file")
        return load_csv(filename)
    else:
        print("Cannot load file. File must be in csv format")


def load_csv(filename:str): # Load CSV data (same technique as basic script)
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

# Calculate highest and lowest grades
# Count students by multiple subjects (Math, Science, etc.)
# Return dictionary with multiple statistics
def analyze_data(students:list):
    stats = {}

    # Calculate highest grade using max()
    highest_grade = max([s["grade"] for s in students])
    stats["highest grade"] = highest_grade

    # Calculate lowest grade using min()
    lowest_grade = min([s["grade"] for s in students])
    stats["lowest grade"] = lowest_grade

    # Calculate overall class average
    stats["average"] = sum([s["grade"] for s in students])/len(students)
    
    # Count the number of studnets for each subject
    for s in students:
        subject = s["subject"]
        if subject in stats:
            stats[subject] += 1
        else:
            stats[subject] = 1
    
    # Get grade distribution
    grades = [s["grade"] for s in students]
    stats["grade distribution"] = analyze_grade_distribution(grades)

    return stats

# Count grades by letter grade ranges
def analyze_grade_distribution(grades:list): 
    distribution = {"A":0, "B": 0, "C":0, "D": 0, "F":0}
    for g in grades:
        if g > 90:
            distribution["A"] += 1
        elif g >80:
            distribution["B"] += 1
        elif g >70:
            distribution["C"] += 1
        elif g >60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return distribution

def save_results(results:dict, filename:str): # Save detailed report
    pass

def main(): # Orchestrate the analysis using all functions
    data = load_data("data/students.csv")
    stats = analyze_data(data)
    print(stats)


if __name__ == "__main__":
    main()
