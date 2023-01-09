print("*******************************")

print(" WELCOME>>>>>>>Eat 24*7<<<<<<<<<<< What's on Your mind?..........")

print("*******************************")

import mysql.connector
import os
import platform

projectdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anu@5806",
    database="foodplaza"

)
mycursor = projectdb.cursor()


def login():
    print("======================================================================================")

    print(" Hey...!! Welcome back...")
    username = input("Enter Username :")
    password = input("enter strong password :")

    print("====================================================================================")

    orderF = input("Do you want to order  (FOOD/DRINKS/BOTH) : ")
    if orderF.lower() == 'food':
        orderFood()


    elif orderF.lower() == 'drinks':
        orderDrinks()

    else:
        orderBoth()


def customerRegistration():
    print("======================================================================================")

    print("Please enter your details here...")

    print("=================================================================")
    L = []
    cust_name = input("Enter Your Name: ")
    L.append(cust_name)
    cust_age = input("Enter Your Age: ")
    L.append(cust_age)
    cust_address = input("Enter  Your Address: ")
    L.append(cust_address)
    cust_location = input("Enter  Your location: ")
    L.append(cust_location)
    cust_phonenum = input("Enter phone number : ")
    L.append(cust_phonenum)
    username = input("Enter username : ")
    L.append(username)
    password = input("Enter Strong password: ")
    L.append(password)
    customer = (L)
    sql = "insert into customer_registration(cust_name,cust_age, cust_address,cust_location, cust_phonenum, username,password) values (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, customer)
    projectdb.commit()
    sql1 = "insert into login select username,password from customer_registration"
    mycursor.execute(sql1)
    projectdb.commit()

    print("===========================================================================================")

    print("Congratulations.....!!!!  Your Registration is Completed........")
    print("....Please login with your Username and password....")
    print(".... Have a nice day...")

    login()

    print("===========================================================================================")


def ViewFood():
    mycursor.execute("select * from food_table")
    result = mycursor.fetchall()
    for x in result:
        print(x)


def ViewDrinks():
    mycursor.execute("SELECT * FROM drinks_table ")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def orderDrinks():
    print("=============================================================================")
    print("DRINKS")
    print("=============================================================================")

    mycursor.execute("SELECT * FROM drinks_table ")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("==============================================================================")

    L = []
    customer_name = input("Enter your name : ")
    L.append(customer_name)
    drink_id = input("Please enter the id of the drink do u want : ")
    L.append(drink_id)

    print("======================================================================================")

    sql = "select * from delivery_person where status='available'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("======================================================================================")

    D_id = int(input("Enter the id of the delivery person : "))
    L.append(D_id)

    print("======================================================================================")

    sql = "select * from drinks_table where drink_id= %s"
    did = (drink_id,)
    mycursor.execute(sql, did)
    myresult = mycursor.fetchall()
    for y in myresult:
        print('Drink details : ')
        print(y)

    print("======================================================================================")

    price = int(input("Enter price of the drink : "))
    L.append(price)
    quantity_item = int(input("Enter quantity : "))
    L.append(quantity_item)
    total_price = price * quantity_item
    L.append(total_price)
    Orderdrink = (L)
    sql1 = "insert into orderdrinks(customer_name,drink_id,D_id,price,quantity_item,total_price)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql1, Orderdrink)
    projectdb.commit()

    print("============================================================================================")
    print("--------------------Order completed----------------------")
    print("============================================================================================")
    print("Thank you....Proceed to pay")
    print("======================================================================================")

    sql = "select total_price from orderdrinks where customer_name= %s "
    cust = (customer_name,)
    mycursor.execute(sql, cust)
    myresult = mycursor.fetchone()
    for y in myresult:
        print("Total_Amount = ", y)

    V = []
    print("You Have to pay the tip for Delivery person!")

    delivery_tip = int(input(" Enter the Amount : "))
    V.append(delivery_tip)

    print("======================================================================================")

    print(delivery_tip,
          "Thank you for your generous tips for your future orders.They will be passed on to your delivery partner as soon as the orders are delivered ! ")

    print("======================================================================================")

    add = input("Add this tip automatically to future orders (YES/NO) :")
    if add.lower() == 'yes':
        print("Thank you...!")
    else:
        print("++++OHk++++")


    delivery_fee = int(30)
    V.append(delivery_fee)
    payment_amount = total_price + delivery_tip + delivery_fee
    V.append(payment_amount)
    print("Total  amount you have to pay in this order is : ", payment_amount)
    payment_method = input("Enter payment_method (card/Gpay) : ")
    V.append(payment_method)
    pay = (V)
    sql = "insert into proceed_pay (delivery_tip,delivery_fee,payment_amount,payment_method) values (%s,%s,%s,%s)"
    mycursor.execute(sql, pay)
    projectdb.commit()

    print("Your payment Success..thank you")


def orderFood():
    print("======================================================================================")
    print("FOODS")
    print("======================================================================================")

    mycursor.execute("select * from food_table")
    result = mycursor.fetchall()
    for x in result:
        print(x)

    print("======================================================================================")

    L = []
    customer_name = input("Enter your name : ")
    L.append(customer_name)
    food_id = input("Please enter the id of the food do u want : ")
    L.append(food_id)

    print("======================================================================================")

    sql = "select * from delivery_person where status='available'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("======================================================================================")

    D_id = int(input("Enter the id of the delivery person : "))
    L.append(D_id)

    print("======================================================================================")

    sql = "select * from food_table where food_id= %s"
    fid = (food_id,)
    mycursor.execute(sql, fid)
    myresult = mycursor.fetchall()
    for y in myresult:
        print('Food details : ')
        print(y)

    print("======================================================================================")

    price = int(input("Enter price of the food : "))
    L.append(price)
    quantity_item = int(input("Enter quantity : "))
    L.append(quantity_item)
    total_price = price * quantity_item
    L.append(total_price)
    OrderFood = (L)
    sql1 = "insert into orderfood(customer_name,food_id,D_id,price,quantity_item,total_price)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql1, OrderFood)
    projectdb.commit()

    print("============================================================================================")
    print("--------------------Order completed----------------------")
    print("============================================================================================")
    print("Thank you....Proceed to pay")
    print("======================================================================================")

    sql = "select total_price from orderfood where customer_name = %s"
    cust = (customer_name,)
    mycursor.execute(sql, cust)
    myresult = mycursor.fetchone()
    for y in myresult:
        print("Total_Amount = ", y)

    V = []
    print("You Have to pay the tip for Delivery person!")

    delivery_tip = int(input(" Enter the Amount : "))
    V.append(delivery_tip)

    print("======================================================================================")

    print(delivery_tip,
          "Thank you for your generous tips for your future orders.They will be passed on to your delivery partner as soon as the orders are delivered ! ")

    print("======================================================================================")

    add = input("Add this tip automatically to future orders (YES/NO) :")
    if add.lower() == 'yes':
        print("Thank you...!")
    else:
        print("++++OHk++++")

    delivery_fee = int(30)
    V.append(delivery_fee)
    payment_amount = total_price + delivery_tip + delivery_fee
    V.append(payment_amount)
    print("Total  amount you have to pay in this order is : ", payment_amount)
    payment_method = input("Enter payment_method (card/Gpay) : ")
    V.append(payment_method)
    pay = (V)
    sql = "insert into proceed_pay (delivery_tip,delivery_fee,payment_amount,payment_method) values (%s,%s,%s,%s)"
    mycursor.execute(sql, pay)
    projectdb.commit()


def orderBoth():
    L = []
    customer_name = input("Enter your name : ")
    L.append(customer_name)
    print("======================================================================================")
    print("FOODS")
    print("======================================================================================")

    mycursor.execute("select * from food_table")
    result = mycursor.fetchall()
    for x in result:
        print(x)

    print("======================================================================================")

    food_id = input("Please enter the id of the food do u want : ")
    L.append(food_id)

    print("======================================================================================")

    sql = "select * from food_table where food_id= %s"
    fid = (food_id,)
    mycursor.execute(sql, fid)
    myresult = mycursor.fetchall()
    for y in myresult:
        print('Food details : ')
        print(y)

    print("======================================================================================")

    quantity_food = int(input("Enter quantity of food : "))
    L.append(quantity_food)
    price_food = int(input("Enter price of the food : "))
    L.append(price_food)

    print("======================================================================================")
    print("DRINKS")
    print("======================================================================================")

    mycursor.execute("SELECT * FROM drinks_table ")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("======================================================================================")

    drink_id = input("Please enter the id of the drink do u want : ")
    L.append(drink_id)

    print("======================================================================================")

    sql = "select * from drinks_table where drink_id= %s"
    did = (drink_id,)
    mycursor.execute(sql, did)
    myresult = mycursor.fetchall()
    for y in myresult:
        print('Drink details : ')
        print(y)

    print("======================================================================================")

    quantity_drink = int(input("Enter quantity of drink: "))
    L.append(quantity_drink)
    price_drink = int(input("Enter price of the drink : "))
    L.append(price_drink)

    print("======================================================================================")

    food_total = quantity_food * price_food
    L.append(food_total)
    drink_total = quantity_drink * price_drink
    L.append(drink_total)

    print("======================================================================================")

    sql = "select * from delivery_person where status='available'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("======================================================================================")

    D_id = int(input("Enter the id of the delivery person : "))
    L.append(D_id)
    total_price = int(food_total + drink_total)
    L.append(total_price)
    orderBoth = (L)
    sql = "insert into orderboth (customer_name,food_id,quantity_food,price_food,drink_id,quantity_drink,price_drink,food_total,drink_total,D_id,total_price)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, orderBoth)
    projectdb.commit()

    print("============================================================================================")
    print("--------------------Order completed----------------------")
    print("============================================================================================")
    print("Thank you....Proceed to pay")
    print("======================================================================================")

    sql = "select total_price from orderboth where customer_name= %s "
    cust = (customer_name,)
    mycursor.execute(sql, cust)
    myresult = mycursor.fetchone()
    for y in myresult:
        print("Total_Amount = ", y)

    print("======================================================================================")

    V = []
    print("You Have to pay the tip for Delivery person!")

    delivery_tip = int(input(" Enter the Amount : "))
    V.append(delivery_tip)

    print("======================================================================================")

    print(delivery_tip,
          "Thank you for your generous tips for your future orders.They will be passed on to your delivery partner as soon as the orders are delivered ! ")

    print("======================================================================================")

    add = input("Add this tip automatically to future orders (YES/NO) :")
    if add.lower() == 'yes':
        print("Thank you...!")
    else:
        print("++++OHk++++")

    delivery_fee = int(30)
    V.append(delivery_fee)
    payment_amount = total_price + delivery_tip + delivery_fee
    V.append(payment_amount)
    print("Total  amount you have to pay in this order is : ", payment_amount)
    payment_method = input("Enter payment_method (card/Gpay) : ")
    V.append(payment_method)

    pay = (V)
    sql = "insert into proceed_pay (delivery_tip,delivery_fee,payment_amount,payment_method) values (%s,%s,%s,%s)"
    mycursor.execute(sql, pay)
    projectdb.commit()

    print("Your payment Success..thank you")


def deliveryPerson():
    L = []
    D_name = input("Enter Name : ")
    L.append(D_name)
    D_age = input("Enter Age: ")
    L.append(D_age)
    D_phonenum = int(input("Enter Phone number: "))
    L.append(D_phonenum)
    area = input("Enter Area : ")
    L.append(area)
    status = input("Are you available now (AVAILABLE/NOT AVAILABLE) : ")
    if status.lower() == 'available':
        L.append(status)
        delivery = (L)
        sql = "insert into delivery_person (D_name,D_age,D_phonenum,area,status)values (%s,%s,%s,%s,%s)"
        mycursor.execute(sql, delivery)
        projectdb.commit()

    else:
        print("update status when u are available..")


def MenuSet():
    print("*** FOOD ORDERING SYSTEM ***")
    print("** Options are : ***")
    print("Enter 1 : Login Customer")
    print("Enter 2 : Customer Registration ")
    print("Enter 3 : Delivery Person  ")
    print("Enter 4 :  View  Food")
    print("Enter 5 : View Drinks")
    print("Enter 6 : SignOut")

    print("***************")
    try:  # Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: "))  # Will Take Input From User
    except ValueError:
        exit("\nHy! That's Not A Number")  # Error Message
    else:
        print("\n")  # Print New Line
        if (userInput == 1):
            exist = input("Do u have an account (Y/N) : ")
            if exist.lower() == 'y':
                login()
            else:
                print("Go to Registration")
                customerRegistration()
        elif (userInput == 2):
            customerRegistration()
        elif (userInput == 3):
            deliveryPerson()
        elif (userInput == 4):
            ViewFood()
        elif (userInput == 5):
            ViewDrinks()
        elif (userInput == 6):
            MenuSet()


        else:
            print("Enter correct choice. . .  ")


MenuSet()


def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while (runAgn.lower() == 'y'):
        if (platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        runAgn = input("\nwant To Run Again Y/n: ")


runAgain()
