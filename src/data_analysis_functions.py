# TODO

# Generic loader that checks file extension
def load_data(filename): 
    # Check for
    if filename.endswith(".csv"):
        print("Processing csv file")
        return load_csv(filename)
    else:
        print("Cannot load file. File must be in csv format")


def load_csv(filename): # Load CSV data (same technique as basic script)
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

def analyze_data(students): # Return dictionary with multiple statistics
    pass

def analyze_grade_distribution(grades): # Count grades by letter grade ranges
    pass

def save_results(results, filename): # Save detailed report
    pass

def main(): # Orchestrate the analysis using all functions
    data = load_data("data/students.csv")


if __name__ == "__main__":
    main()
