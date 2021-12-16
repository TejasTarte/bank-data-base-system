import mysql.connector
import program as p

mydb = mysql.connector.connect(host='localhost',  #   Here our host is local host
                               user='root',
                               password='password',  # enter your password in password section
                               database='bankdb')

mycursor = mydb.cursor()

# main run program
while True:
    p.menu()
    lett = input('Enter choice: ')
    if lett == '1':
        p.create()
    elif lett == '2':
        p.show_details()
    elif lett == '3':
        p.update()
    elif lett == '4':
        p.delete()
    elif lett == '5':
        p.search_menu()
        z = input()
        if z == 'A' or 'a':
            p.search_acc()
        elif z == 'B' or 'b':
            p.search_name()
        else:
            print('INVALID INPUT')
    elif lett == '6':
        print('EXITING.....')
        break

    else:
        print('Invalid INPUT')
