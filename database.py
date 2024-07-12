import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host="localhost",user="root",password="ajinisarockstar",database="hehe")
    mycursor=mydb.cursor()
    mycursor.execute("select*from employee")
    result = mycursor.fetchmany()
    mycursor.close()
    mydb.close()
    return result