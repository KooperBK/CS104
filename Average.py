#CS104
#Kooper Kaney
#Average

total = 0
average = 0
howManyEntered = 0

howMany = int(input('How many test scores would you like to average? '))
while howManyEntered < howMany:
    testscore = int(input('Enter test score: '))
    total = total + testscore
    howManyEntered += 1
average = total / howMany
print(f'The average for the test scores you entered is: {average:.1f}')

                    
