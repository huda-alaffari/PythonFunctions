def grade_exam(num_q, mark_for_each):  
    sum_mark = 0
    answer = input("Enter answer for {} Question".format(num_q))
    Uanswre = input("Enter your answer: ")
    for i in range(len(answer)):
        if(Uanswre[i] == answer[i]):
            sum_mark+= mark_for_each      
    print(sum_mark, "out of", len(answer)*mark_for_each)
grade_exam(12,2)
    
