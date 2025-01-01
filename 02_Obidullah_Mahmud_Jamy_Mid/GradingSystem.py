def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    else:
        return 'F'

def class_performance(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
    
    if average_score > 85:
        performance = "Excellent Performance"
    elif 70 <= average_score <= 85:
        performance = "Satisfactory Performance"
    else:
        performance = "Needs Improvement"
    
    return average_score, performance



    
