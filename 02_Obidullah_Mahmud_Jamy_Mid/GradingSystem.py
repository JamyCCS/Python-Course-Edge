def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif score>100:
        return 'Invalid Score'
    else:
        return 'F'
    

def class_performance(scores_dict):
    total_score = sum(scores_dict.values())
    average_score = total_score / len(scores_dict)
    
    if average_score > 85:
        performance = "Excellent Performance"
    elif 70 <= average_score <= 85:
        performance = "Satisfactory Performance"
    else:
        performance = "Needs Improvement"
    
    return average_score,performance


n=int(input("Enter the number of students: "))

resultbook = {}

for i in range(n):
    student_score = int(input("Enter student score: "))
    grade = calculate_grade(student_score)
    print(f"Grade is {grade}\n")
    resultbook[i] = student_score


average_score, performance = class_performance(resultbook)
print(f"The class Average is {average_score} and the class performance is {performance}")


    
