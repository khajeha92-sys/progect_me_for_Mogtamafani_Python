#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#PROJECT OF CLASS2

#1.Maryam needs to check if a year is a leap year.Rules:
def leap_year_checker(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')

#2.Maryam is preparing for a trip and wants to classify temperatures...
def temperature_classifier(x):
    if x > 30:
        print('Its Hot')
    elif 20 <= x < 30:
        print('Its Warm')
    elif 10 <= x < 19:
        print('Its Cool')
    elif x < 10:
        print('Cold')
    else:
        print('Pleas Enter number ! ')

#3.Hamed uses a 34-hour clock.Calculate what time he'llwake up after sleep
#a certain number of hours.
def alarm_clock(curr, sleep):
    y = sleep % 24
    summ = curr + y
    print(f'Wake up at {summ:02}:00 .')

#4.Maryam is hosting a party with 7 friends. she orders 24 slices of pizza.
# Calculate how mary slices each person gets and how many are left for her chicken.
def party_planner(slices, people):
    return divmod(slices, people)

#5.Hamed has $10,000 in his bank account with 8% annual interest, compounded monthly.
#Calculate the final amount after t years.
def bank_interest_calcuiator(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A
#6.
def valid_score(sub):
    while True:
        try:
            score = float(input(f'Enter{sub} score(0-100) : '))
            if 0 <= score <= 100:
                return score
            else:
                print('it must be 0-100')
        except:
            print('Enter valid number')
def calulate(score):
    if score >= 90:
        return 'A', 'Excellent'
    elif score >= 80:
        return 'B', 'Good'
    elif score >= 70:
        return 'C', 'Satisfactory'
    elif score >=60:
        return 'D', 'Needs Imrovement'
    else:
        return 'F', 'Requires Attention'
def student_info():
    print('\n Enter Student info')
    name = input('Name: ').strip()
    if not name:
        name = 'Un name'
        print(name)
    stu_id = input('Enter id: ').strip()
    if not stu_id:
        stu_id = 'no id'
    return { 'name': name, 'id': stu_id}
def generate(name, student, scores, average, grade, status, passed):
    report = []
    subjects = ['Math', 'Science', 'English']
    report.append('-'*30)
    report.append(f"{'Grade report':^30}")
    report.append('-'*30)
    report.append(f"{'Nam':<20}: {name}")
    report.append(f"{'ID':<20}: {student}")
    report.append('-'*30)
    for i, subject in enumerate(subjects):
        sub_grade, _ = calulate(scores[i])
        report.append(f"{subject:<15}:{scores[i]:>6.1f} (Grade: {sub_grade})")
    report.append('-'*30)
    report.append(f"{'Average':<15}: {average:>6.1f} (Grade: {grade})")
    report.append('-'*30)
    report.append(f"{'Status':<20}: {status}")
    report.append(f"{'Result':<20}: {'passed' if passed else 'failed'}")

    return '\n'.join(report)
def MM():
    print('-'*30)
    print(f"{'Grade' :^60}")
    print('-'*30)

    try :
##    status = 'm'
        student = student_info()
        math = valid_score('math')
        science = valid_score('science')
        english = valid_score('english')
        scores = [math, science, english]
        average = sum(scores) / len(scores)
        grade, status = calulate(average)
        passed = average >= 60
        report = generate(student['name'], student['id'], scores, average, grade, status, passed)
        print(f'\n {report}')
        if passed:
            if grade == 'A':
                print('\n Outstanding performance')
            else:
                print('\n Keep up the good work')
        else:
            print('\n Need impovement.Consider extra help')

    except KeyboardInterrupt:
        print('\n\n Program interrupted.Exiting...')
    except Exception as e:
        print(f'\n An error occurred:{e}')
            
#7.       
def proper(leng, wid):
    area = leng * wid
    primeter = 2 * (leng + wid)
    return (area, primeter)
def ma():
    leng = float(input('Enter length: '))
    wid = float(input('Enter width:'))
    area, primeter = proper(leng, wid)
    print(f"Area: {area:.2f}")
    print(f"Preimeter: {primeter:.2f}")
    
#8.
def c_fahrenheit(cel):
    return (cel * 9 / 5) + 32
def maa():
    cel = float(input('Enter temperature:'))
    fah = c_fahrenheit(cel)
    print(f"{cel:.1f}C = {fah:.1f}F")

def main():
    print('Project 1. Leap Year: ')
    year = int(input('Enter your Year: '))
    leap_year_checker(year)
    print('*'*90)
    print('Project 2.Temperature Classifier : ')
    temp = int(input('Enter your temprature : '))
    temperature_classifier(temp)
    print('*'*90)
    print('Project 3.Hameds Sleep Schedule : ')
    curr = 13
    sleep = 50
    alarm_clock(curr, sleep)
    print('*'*90)
    print('Project 4. Maryam and Friends : ')
    result = party_planner(24, 7)
    print(result)
    print('*'*90)
    print('Project 5. Hameds Saving : ')
    Expected = bank_interest_calcuiator(10000, 0.08, 12, 1)
    print(f'${Expected:,.2f}')
    print('*'*90)
    print('Project 6.  ')
    if __name__ == '__main__':
        MM()
        print('*'*90)
        print('Project 7. ')
        ma()
        print('*'*90)
        print('Project 8. ')
        maa()
        print('THE END')
###Driver Code###
main()    



#AMIRABAS KHAJEH
