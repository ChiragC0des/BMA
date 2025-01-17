# Get the number of students present
num_students = int(input("Enter the number of students present: "))

# Function to calculate average marks
def cal_avg():
    total = 0
    # Get marks for each subject and ensure they are integers
    maths = int(input("Enter the marks for Maths: "))
    chemistry = int(input("Enter the marks for Chemistry: "))
    physics = int(input("Enter the marks for Physics: "))
    
    # Calculate total and average
    total = maths + chemistry + physics
    avg = total / 3
    return avg

# List to store averages of each student
averages = []

# Loop through each student to calculate their average
for student in range(1, num_students + 1):
    print(f"\nEntering marks for Student {student}:")
    avg = cal_avg()  # Call the function to calculate average
    averages.append(avg)  # Store the average in the list

# Display the averages for all students
print("\nListings of averages for all students in ascending order:")
averages.sort()
for student, avg in enumerate(averages, start=1):
    print(f"Student {student}: {avg:.2f}")
