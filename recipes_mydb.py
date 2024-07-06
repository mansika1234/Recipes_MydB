import os
import platform
import datetime
import mysql.connector as sqltor
global z
mydb=sqltor.connect(user="root", passwd="mansika",host="localhost", database="recipes")
print("connected")
mycursor=mydb.cursor()
def add_recipe():
    dish=input("Enter the Dish name:")
    ing=input("Enter the ingredients required:")
    steps=input("Enter the instructions:")
    ins="INSERT INTO recipe (dish, ing,steps)VALUES (%s,%s,%s)"
    data = (dish, ing, steps)
    mycursor.execute(ins,data)
    mydb.commit()
    print("Recipe added successfully!")

def view_recipe():
       print("do u want to view the recipe ?")
       sel="SELECT * FROM recipe"
       mycursor.execute(sel)
       recipe=mycursor.fetchall()

       if not recipe:
        print("No recipe found.")
        return
    
       for recipe in recipe:
        print(f"Dish: {recipe[0]}")
        print(f"Ing: {recipe[1]}")
        print(f"Steps: {recipe[2]}")

def search_recipe():
    key=input("Enter a keyword to search for a recipe:")
    ser="SELECT * FROM recipe WHERE dish LIKE %s OR ing LIKE %s"
    data = ("%" + key + "%", "%" + key + "%")
    mycursor.execute(ser,data)
    recipe=mycursor.fetchall()

    if not recipe:
        print("No matching recipe found.")
        return
    for recipe in recipe:
        print(f"Dish: {recipe[0]}")
        print(f"Ing: {recipe[1]}")
        print(f"Steps: {recipe[2]}")

def delete_recipe():
    sel="SELECT * FROM recipe"
    mycursor.execute(sel)
    recipe=mycursor.fetchall()

    if not recipe:
         print("No recipes found.")
         return

    view_recipe()

    dish=input("Enter the Dish Name to delete:")

    delt="DELETE FROM recipe WHERE  dish = %s"
    data = (dish,)
    
    mycursor.execute(delt,data)
    mydb.commit()

    if mycursor.rowcount == 0:
        print("Invalid Dish Name.")
        return

    print(f"Recipe with Dish Name '{dish}' deleted successfully!")

def menu():
     while True:
        print("--- Recipe Manager ---")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Search Recipe")
        print("4. Delete Recipe")
        print("5. Exit")

        choice=input("Enter your choice[1-5]:")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipe()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            delete_recipe()
        elif choice == "5":
            print("Exiting Recipe Manager...")
            break
        else:
            print("Invalid choice. Try Again!")

menu()

mydb.close()
