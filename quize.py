def entry(answer):
    REG_NO = int(input('enter the register number'))
    name=input('enter the name >>')
    values = (REG_NO,name,answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9])
    good = ("INSERT INTO `entry`(reg_no,`name`, `ans1`, `ans2`, `ans3`, `ans4`, `ans5`, `ans6`, `ans7`, `ans8`, `ans9`, `ans10`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    play.execute(good,values)
    quize.commit()
import mysql.connector
quize = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="quize")
play = quize.cursor()
answer = ()   
qustions = ['1.what is latest version of android ?',
            '2.How many bytes is an int in Python?',
            '3.what is latest version of windows ?',
            '4.what is latest version of iphone ?',
            '5.what is extension of java file ?',
            '6.what is extension of golang ?',
            '7.when was fb launched in india ?',
            '8.what is syntax for print statment in python ?',
            '9.when was facebook founded ?',
            '10.when was instagram founded ?',]
for i in range(len(qustions)):
    print(qustions[i])
    ans = input()
    answer=list(answer)
    answer.insert(i,ans)
entry(answer)

correct_answer = ('android 10','16 bytes','windows 10','iphone 11','.java','.go','2006','print()','2004','2010')

for i in range(len(answer)):
    if(answer[i] == correct_answer[i]):
        print(correct_answer[i], '= = = correct')
    else:
        print(answer[i], '= = = incorrect')
        


    
    
