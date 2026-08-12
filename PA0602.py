#Use built-in modules to perform complex operations

import statistics 


#1. Calculate the mean of the student marks using statistics.mean().

data =[75, 80, 90, 85, 70, 95]
mean_marks = statistics.mean(data)
print(f'Mean of student marks: {mean_marks}')

#2. Calculate the median mark using statistics.median().
median_marks = statistics.median(data)
print(f'Median of student marks: {median_marks}')


