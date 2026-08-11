#Constructing and analyzing branching statements 

average = 68
if average >= 75:
    result = "Distinction"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"
    
print(result)        
        
        
#1. The output that would be displayed is "Pass"
#2.Because the average is 68. The first condition 'average >= 75' is False,
#So it checks the next condition 'average >= 50'. Since 68 >=50 is True,
# result is set to 'Pass'. The else block is skipped.add()
#3.Fail, 48 is not >= 75 and not >=50, so it goes to the else block
#4.Distinction, 80 >= 75 is True, so result is set to "Distinction"immediately         