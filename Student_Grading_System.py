def calculate_grade(total_marks):# Function to calculate student grade based on his score
    if total_marks >= 90:
        return 'A+'
    elif total_marks >= 80:
        return 'A'
    elif total_marks >= 70:
        return 'B+'
    elif total_marks >= 60:
        return 'B'
    elif total_marks >= 50:
        return 'C'
    elif total_marks >= 40:
        return 'P'
    else:
        return 'Fail'

def calculate_percentage(total_marks, max_total_marks):#calculate the percentage
    return (total_marks / max_total_marks) * 100

def calculate_subject_total(fa1, fa2, sa):#calculate total marks for a subject
    return fa1 + fa2 + sa

def school_grading_system():
    subjects = ["Telugu", "Hindi", "English", "Mathematics", "Science", "Social"]
    max_fa_marks = 25 * 2  # Max marks for two formative assessments
    max_sa_marks = 50  # Max marks for one summative assessment
    max_subject_marks = max_fa_marks + max_sa_marks
    total_max_marks = max_subject_marks * len(subjects)  # Maximum possible marks for all subjects

    # Input student details
    name = input("Enter the name of the student: ")
    total_marks = 0

    for subject in subjects:
        print(f"\n--- {subject} ---")
        fa1 = float(input(f"Enter marks for Formative Assessment 1 (out of 25) in {subject}: "))
        fa2 = float(input(f"Enter marks for Formative Assessment 2 (out of 25) in {subject}: "))
        sa = float(input(f"Enter marks for Summative Assessment (out of 50) in {subject}: "))
        # Calculate total marks for the subject
        subject_total = calculate_subject_total(fa1, fa2, sa)
        print(f"Total marks for {subject}: {subject_total}/{max_subject_marks}")
        total_marks += subject_total

    percentage = calculate_percentage(total_marks, total_max_marks)# Calculate percentage
    overall_grade = calculate_grade(percentage)# Calculate overall grade

    # Input student attendance
    total_classes = int(input("\nEnter the total number of classes held: "))
    attended_classes = int(input("Enter the number of classes attended: "))
    attendance_percentage = calculate_percentage(attended_classes, total_classes)# Calculate attendance percentage

    # Output final results
    print(f"\n{name}'s Total Marks: {total_marks}/{total_max_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Overall Grade: {overall_grade}")
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

school_grading_system()
