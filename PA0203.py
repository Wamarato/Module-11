#Change the  value to test different results

average_mark = 68 #test case 1 Pass/Component

#Branching statement to determine performance level
if average_mark >= 75 and average_mark <= 100 :
    performance_level = "Distinction"
elif average_mark >= 60 and average_mark <= 74 :
        performance_level = "Component"
elif average_mark >= 50 and average_mark <= 59:
    performance_level ="Pass"
elif average_mark >=-0 and average_mark <=49:
    performance_level = "Not Yet Component"
else:
    performance_level = "Invalid Mark"                


print("performance_level:", performance_level )        
