import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password="naveen",database="ATM_MACHINE")
c1=conn.cursor()
print('''========================================================================
========''')

print("WELCOME TO OUR ATM")

print('''========================================================================
========''')

print("1.To create account")
print("2.To login")
print("3.Exit")
print('''========================================================================
========''')

op=int(input(&quot;Enter your choice :&quot;))
print'''========================================================================
=======''')

if op==1:
    c="y"
    while c=="y":
        m=int(input("Enter a 4 digit number as accont number:"))
        cb="select * from records where ACCONT_NO={}".format(m)
        c1.execute(cb)
        d=c1.fetchall()
        data=c1.rowcount
        if data==1:
            print('''================================================================================''')
            print("This account number already exists:")
            c=input("Do you want to continue y/n ")
            print('''================================================================================''')
            if c=="y":
                continue
            else:
                print("Thank you")
                print("PLEASE CLOSE THIS FILE BEFORE EXITING")
                print("Visit again")
                print('''================================================================================''')
        else:
            name=input("Enter your name:")
            passw=int(input("Enter your pass word:"))
            ab="insert into records(ACCONT_NO,PASSWORD,NAME) values({},{},{};)".format(m,passw,name)
            print('''================================================================================''')
            c1.execute(ab)
            conn.commit()
            print("Account sucessfully created")
            print("The minimum balance is 1000")
            print('''================================================================================''')
            s=int(input("Enter the money to be deposited :"))
            print('''========================================================================
========''')
            sr="update records set CR_AMT={} where ACCONT_NO={}".format(s,m)
            c1.execute(sr)
            conn.commit()
            ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(m)
            c1.execute(ef)
            conn.commit()
            print("sucessfully deposited")
            print("Thank you")
            print("PLEASE CLOSE THIS FILE BEFORE EXITING")
            print("Visit again")
            break
elif op==2:
    y="y"
    while y=="y":
        acct=int(input("Enter your account number:"))
        cb="select * from records where ACCONT_NO={}".format(acct)
        c1.execute(cb)
        c1.fetchall()
        data=c1.rowcount
        if data==1:
            pas=int(input("Enter your password :"))
            print('''========================================================================
========''')
            e="select password from records where ACCONT_NO={}".format(acct)
            c1.execute(e)
            a=c1.fetchone()
            d=list(a)
            if pas==d[0]:
                print("correct")
                print("1.Depositng money:")
                print("2.withdrawing money&quot;)
                print("3.Transfering money:")
                print("4.Checking balance&quot;)
                print("5.Changing Account number:")
                print("=========================================================================")
                r=int(input("Enter your choice:))
                print(================================================================================")
                if r==1:
                    amt=int(input("Enter the money to be deposited:"))
                    print("================================================================================")
                    sr="update records set CR_AMT=CR_AMT + {} where ACCONT_NO={}".format(amt,acct)
                    c1.execute(sr)
                    conn.commit()
                    ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(acct)
                    c1.execute(ef)
                    conn.commit()
                    print("sucessfully deposited";)
                    t=input("Do you want to continue y/n -")
                    print('''================================================================================''')
                    if t=="y":
                        continue
                    else:
                        print("Thank you"end=)
print(&quot; PLEASE CLOSE THIS FILE BEFORE EXITING&quot;)
if r==2:
amt=int(input(&quot;Enter the money to withdraw:&quot;))
print(&quot;========================================================================
========&quot;)

22

ah=&quot;select BALANCE from records where accont_no={}&quot;.format(acct)
c1.execute(ah)
m=c1.fetchone()
if amt &gt;m[0]:
print(&quot;Your are having less than&quot;,amt)
print(&quot;Please try again&quot;)
print(&quot;========================================================================
========&quot;)

else:
sr=&quot;update records set balance=balance - {} where
ACCONT_NO={}&quot;.format(amt,acct)
ed=&quot;update records set WITHDRAWL ={} where
ACCONT_NO={}&quot;.format(amt,acct)
c1.execute(ed)
c1.execute(sr)
conn.commit()
print(&quot;Sucessfully updatad&quot;)
y=input(&quot;do you want to continue y/n -&quot;)
if y==&quot;y&quot;:
continue
else:
print(&quot; Thank you&quot;)
print(&quot; PLEASE CLOSE THIS FILE BEFORE EXITING&quot;)

if r==3:
act=int(input(&quot;Enter the accont number to be transferrsd :&quot;))

print(&quot;========================================================================
========&quot;)

cb=&quot;select * from records where ACCONT_NO={}&quot;.format(act)
c1.execute(cb)
c1.fetchall()
data=c1.rowcount
if data==1:
print(act ,&quot;number exists&quot;)

23

m=int(input(&quot;Enter the money to be transferred :&quot;))

print(&quot;========================================================================
========&quot;)

ah=&quot;select BALANCE from records where accont_no={}&quot;.format(acct)
c1.execute(ah)
c=c1.fetchone()
if m &gt; c[0]:
print(&quot;Your are having less than&quot;,m)
print(&quot;Please try again&quot;)

print(&quot;========================================================================
========&quot;)

else:
av=&quot;update records set balance=balance-{} where
ACCONT_NO={}&quot;.format(m,acct)
cv=&quot;update records set balance=balance+{} where
ACCONT_NO={}&quot;.format(m,act)
w=&quot;update records set withdrawl=withdrawl+{} where
accont_no={}&quot;.format(m,acct)
t=&quot;update records set CR_AMT=CR_AMT+{} where
accont_no={}&quot;.format(m,act)
c1.execute(av)
c1.execute(cv)
c1.execute(w)
c1.execute(t)
conn.commit()
print(&quot;Sucessfully transfered&quot;)
y=input(&quot;do you want to continue y/n -&quot;)
if y==&quot;y&quot;:
continue
else:
print(&quot; Thank you&quot;)
print(&quot; PLEASE CLOSE THIS FILE BEFORE EXITING&quot;)
if r==4:

24

ma=&quot;select balance from records where accont_no={}&quot;.format(acct)
c1.execute(ma)
k=c1.fetchone()
print(&quot;Balance in your account=&quot;,k)
print(&quot;========================================================================
========&quot;)

y=input(&quot;do you want to continue y/n -&quot;)
if y==&quot;y&quot;:
continue
else:
print(&quot; Thank you&quot;)
print(&quot; PLEASE CLOSE THIS FILE BEFORE EXITING&quot;)
if r==5:
i=int(input(&quot;Enter your new account number:&quot;))
cb=&quot;select * from records where ACCONT_NO={}&quot;.format(i)
c1.execute(cb)
c1.fetchall()
data=c1.rowcount
if data==1:
print(&quot;This number already exists&quot;)
print(&quot;Try again&quot;)

y=input(&quot;do you want to continue y/n -&quot;)
if y==&quot;y&quot;:
continue
else:
print(&quot; Thank you&quot;)
print(&quot; PLEASE CLOSE THIS FILE BEFORE EXITING&quot;)
else:
name=input(&quot;Enter your name&quot;)
ar=&quot;Update records set accont_no={} where name=&#39;{}&#39; and
password={}&quot;.format(i,name,pas)
c1.execute(ar)
conn.commit()
print(&quot;Your new account number is &quot;,i)
else:

25

print(&quot;Wrong password&quot;)
print(&quot;========================================================================
========&quot;)

y=input(&quot;do you want to continue y/n -&quot;)

else:
print(&quot;your Account does not exists&quot;)

if op==3:
print(&quot;Exiting&quot;)
print(&quot;Please close this file before exiting.&quot;)
c1.close()
