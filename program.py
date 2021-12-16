import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='password',  # enter your database password
                               database='bankdb')

mycursor = mydb.cursor()

def menu():
    print('*'*170)
    print('MENU'.center(100))
    print()
    print('1. Insert a record'.center(100))
    print('2. Display record'.center(100))
    print('3. Update a record'.center(100))
    print('4. delete a record'.center(100))
    print('5. search a record'.center(100))
    print('6. Exit'.center(100))
    print('*' * 170)


# search meanu
def search_menu():
    print('A. search by Acc_no (press a/A)')
    print('B. search by Acc_Name (press b/B)')
    print('*'*180)

# create table
def create():
    try:
        query = "CREATE TABLE Details (ACCNo INT(20) primary key NOT NULL ,Name VARCHAR(55) NOT NULL," \
                "PhoneNo VARCHAR(12) NOT NULL, Address VARCHAR(255),Email VARCHAR(40)," \
                "City VARCHAR(25),Country VARCHAR(255)) "
        mycursor.execute(query)
        print('Table created')
        insert()
    except:
        print('Table already existed')
        insert()

# inserting values
def insert():
    while True:
        acc = input('Enter Acc no: ')
        name = input('Enter Name : ')
        mob = input('Enter Mob No: ')
        address = input('Enter address: ')
        email = input('Enter email: ')
        city = input('Enter city: ')
        country = input('Enter country: ')
        val = [acc,name.upper(),mob,address.upper(),email,city.upper(),country.upper()]
        query = "INSERT INTO Details VALUES (%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,val)
        mydb.commit()
        print()
        print('RECORD SUCCESSFULLY ENTERED....')
        print('*'*100)

        # check if user needs to enter some more records
        print('Would you like to enter some more record.')
        lett = input('Type "N" or "n" to return back to menu: ')
        if lett == 'N' or lett == 'n':
            break

# show details or display details
def show_details():
    query = 'SELECT * FROM Details'
    mycursor.execute(query)
    result = mycursor.fetchall()
    f = '%23s %23s %23s %23s %23s %23s %23s '
    print(f % ('ACC_NO','NAME','PHONE NO','ADDRESS','EMAIL','CITY','COUNTRY'))
    for i in result:
        for j in i:
            print('%23s' % j, end=' ')
        print()

# update record
def update():
    query = 'SELECT * FROM Details'
    mycursor.execute(query)
    result = mycursor.fetchall()
    A = int(input('Enter ACC_NO to be updated: '))
    for i in result:
        # convert to list
        i = list(i)
        # selecting acc no
        if i[0] == A:
            lett = input('Change Name (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[1]=input('Enter name: ')
                i[1]=i[1].upper()

            lett = input('Change Phone_no (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[2] = input('Enter Phone no: ')
                i[2] = i[2]

            lett = input('Change Address (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[3] = input('Enter Address: ')
                i[3] = i[3].upper()

            lett = input('Change Email_id (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[4] = input('Enter Email_id: ')
                i[4] = i[4].upper()

            lett = input('Change City (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[5] = input('Enter City: ')
                i[5] = i[5].upper()

            lett = input('Change Country (Y / y) : ')
            if lett == 'Y' or lett == 'y':
                i[6] = input('Enter Country: ')
                i[6] = i[6].upper()


            query = 'UPDATE Details SET Name = %s, PhoneNo = %s,' \
                    'Address = %s, Email = %s, City = %s, Country = %s WHERE ACCNo = %s'
            val = (i[1],i[2],i[3],i[4],i[5],i[6],i[0])
            mycursor.execute(query,val)
            mydb.commit()
            print('ACCOUNT UPDATED......')
            break

        else:
            print('NO MATCH FOUND.......')

# delete account
def delete():
    while True:
        query = 'SELECT * from Details'
        mycursor.execute(query)
        result = mycursor.fetchall()
        A = int(input('Enter ACC_No to be deleted: '))
        for i in result:
            i = list(i)
            if i[0] == A:
                query = 'DELETE FROM Details WHERE ACCNo = {}'.format(i[0])
                mycursor.execute(query)
                # or ve can use
                # query = 'DELETE FROM Details WHERE ACCNo = %s'
                # val = (i[0],)
                # mycursor.execute(query,val)
                mydb.commit()
                print('RECORD SUCCESSFULLY DELETED...')
                break
        else:
            print('NO RECORD FOUND....')

        # ask user if he want to delete more records
        print('press n/N to go back to main menu or \npress y/Y to delete more records')
        z = input()
        if z == 'N' or z == 'n':
            break

# search programmm for account
def search_acc():
    query = 'select * from Details'
    mycursor.execute(query)
    result = mycursor.fetchall()
    A = int(input('Enter the Acc_no to be searched : '))
    for i in result:
        if i[0] == A:
            f = '%23s %23s %23s %23s %23s %23s %23s '
            print(f % ('ACC_NO', 'NAME', 'PHONE NO', 'ADDRESS', 'EMAIL', 'CITY', 'COUNTRY'))
            for j in i:
                print('%23s' % j, end=' ')
            print()
            break

    else:
        print('NO RECORD FOUND...')

# search programm by name
def search_name():
    query = 'select * from Details'
    mycursor.execute(query)
    result = mycursor.fetchall()
    A = input('Enter the Acc_holder Name to be searched : ')
    A = A.upper()
    for i in result:
        if i[1] == A:
            f = '%23s %23s %23s %23s %23s %23s %23s '
            print(f % ('ACC_NO', 'NAME', 'PHONE NO', 'ADDRESS', 'EMAIL', 'CITY', 'COUNTRY'))
            for j in i:
                print('%23s' % j, end=' ')
            print()
            break

    else:
        print('NO RECORD FOUND...')
