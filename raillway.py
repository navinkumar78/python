import mysql.connector
import random 
import os
#import pandas as pd 

mydb=mysql.connector.connect(host="localhost",user="root",passwd="aims",database="reservation")
if mydb.is_connected():
    print("sucessfully connected to mysql database")
mycursor=mydb.cursor()

def railresmenu():
                print('''
                    ###############################################################################################################
                      
                    *     ######     ######   ###########  #         #          #  ######  #       #
                          #     #   #      #       #       #         #          # #      #  #     #
                          #      #  #      #       #       #         #          # #      #   #   #
                          #     #   #      #       #       #         #          # #      #    # #
                          ######    ########       #       #         #    ##    # ########     #
                          #     #   #      #       #       #         #   #  #   # #      #     #
                          #     #   #      #       #       #         #  #    #  # #      #     #
                          #     #   #      #       #       #         # #      # # #      #     #
                          #     #   #      #  ##########   ######### ##        ## #      #     #
                          ''')
                        
              
                print("                  ========*******=======***** ======== WELCOME TO INDIAN RAILWAYS==========*****==========****========")
 
                print('''                                      ################ RAILWAY RESERVATION #############

''')
                print('''                                 =================   1.TRAIN DETAILS   ===================
''')
                print('''                                ==================   2.RESERVATION OF TICKET   ============
''')
                print('''                                ==================   3.CANCELLATON OF TICKET   ============
''')
                print('''                                ==================   4.DISPLAY PNR STATUS     ================
''')
                print('''                               ===================   5. HELP        =================
''')
                print('''                                ===================  6.QUIT   ===================
''')
              
                n=int(input("enter your choice:"))
                if(n==1):
                                traindetail()
                elif(n==2):
                                reservation()
                elif(n==3):
                                cancel()
                elif(n==4):
                                displayPNR()
                elif(n==5):
                                Help()
                elif(n==6):
                                exit(0)
                else:
                                print("wrong choice")
                 
                
def traindetail():
                print("Train Details")
                ch='yes'
                while (ch=='yes'):
                                l=[]
                                name=input("enter train name :")
                                l.append(name)
                                tnum=int(input("enter train number  :"))
                                l.append(tnum)
                                ac1=int(input("enter number of AC 1 class seats"))
                                l.append(ac1)
                                ac2=int(input("enter number of AC 2 class seats"))
                                l.append(ac2)
                                ac3=int(input("enter number of AC 3 class seats"))
                                l.append(ac3)
                                slp=int(input("enter number of sleeper class seats"))
                                l.append(slp)
                                train=(l)
                                sql="insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
                                mycursor.execute(sql,train)
                                mydb.commit()
                                print("insertion completed")
                                mycursor.execute("select * from traindetail")
                                data=mycursor.fetchall()
                                for row in data:
                                    print(list(row))
                                print("Do you want to insert more train Detail")
                                ch=input("enter yes/no:")
                                if ch=="no":
                                    break
                print('\n' *10)

                print("===============================================================================================================================================")
                railresmenu()
def reservation():
                
                mycursor.execute("select * from traindetail")
                data=mycursor.fetchall()
                for row in data:
                    print(row)
                l1=[]
                pname=input("enter passenger name:")
                l1.append(pname)
                age=input("enter age of passenger:")
                l1.append(age)
                trainno=input("enter your train number from above list:")
                l1.append(trainno)
                fr=input("enter boarding station name:")
                l1.append(fr)
                to=input("enter departure station name:")
                l1.append(to)
                np=int(input("Enter number of passenger:"))
                l1.append(np)
                print("select a class you would like to travel in")
                print("1.AC FIRST CLASS")
                print("2.AC SECOND CLASS")
                print("3.AC THIRD CLASS")
                print("4.SLEEPER CLASS")
                cp=int(input("Enter your choice:"))
                if(cp==1):
                                amount=np*1000
                                cls='ac1'
                elif(cp==2):
                                amount=np*800
                                cls='ac2'
                elif(cp==3):
                                amount=np*500
                                cls='ac3'
                else:
                                amount=np*350
                                cls='slp'
                l1.append(cls)           
                print("Total amount to be paid:",amount)
                l1.append(amount)
                pnr=int(random.random()*(10**10-1)+10**9)
                
                print("######  successfully your ticket had booked#########")
                print("PNR Number:",pnr)
                print("status: confirmed")
                sts='conf'
                l1.append(sts)
                l1.append(pnr)
                train1=(l1)
                sql="insert into passengers(pname,age,trainno,fr,DEPARTURE,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,train1)
                mydb.commit()
                print("insertion completed")
                print('\n' *10)

                print("===============================================================================================================================================")
                railresmenu()
                railresmenu()
def cancel():
                print("Ticket cancel window")
                pnr=input("enter PNR for cancellation of Ticket:")
                pn=(pnr,) 
                sql="update passengers set status='deleted' where pnrno=%s"
                mycursor.execute(sql,pn)
                mydb.commit()
                print("YOUR TRAIN TICKET HAS BEEN CANCELED")
                print("YOU CAN GO BACK TO HOME")
                print('\n' *10)

                print("=================================================================================================================================================")
                railresmenu()
                railresmenu()
def displayPNR():
    print("PNR STATUS window")
    pnr = input("enter PNR NUMBER:")
    pn = (pnr,)
    sql = "select * from passengers where pnrno=%s"
    mycursor.execute(sql, pn)
    res = mycursor.fetchall()
    mydb.commit()
    print("PNR STATUS are as follows : ")
    print("pname,age,trainno, noofpas,cls,amt,status, pnrno")
    for x in res:
        print(x)
    
    print("Deletion completed")
    print("Go back to menu")
    print('\n' * 10)
    print("===============================================================================================================================================")
    railresmenu()

                
def Help():
    print('''  Recently railway enquiry DOT telephone numbers have been converted into
3 digit/4 digit at Delhi and some other stations of Northern Railway as well as at
Bombay both on Central and Western Railways. With a view to streamline the
enquiry telephone numbers throughout the Indian Railways and for convenience of
the public, Board vide their letter of even number dated 24.01.91 desired that all
railways may arrange with local MTNL/DOT authorities for enquiry number 131
for the manually attended enquiries and number 1331 etc. for recorded enquiries in
place of the existing numbers.
2. Keeping in view the present day railway enquiry services and the numbering
scheme already implemented at some stations of Northern Railway and at Bombay
Central and Western Railways, it is proposed to standardise the following
numbering scheme with hunting facility:-
Services Telephone Nos./Code
for all stations except
Calcutta – SE Railway
and Bombay– W. Rly.
for Calcutta SE
Railway and
Bombay – W. Rly.
1. General Enquiry 131 132
2. Train arrival status information
(automatic answering)
i) From North Direction/Zone 1331 1341
ii) From East Direction/Zone 1332 1342
iii) From West Direction/Zone 1333 1343
iv) From South Direction/Zone 1334 1344
3. Reservation Enquiry 135
''')


    railresmenu()
railresmenu()
c 
