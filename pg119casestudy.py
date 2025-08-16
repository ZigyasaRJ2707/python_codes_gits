def studentCard(): 

    schoolName = input("enter school name:")
    name = input("enter name of student: ")
    roll = input("enter roll number: ")
    grade = input("enter your class: ")
    section = input("enter your section: ")
    city = input("enter city name: ")
    addressOne = input("enter address line one: ")
    addressTwo = input("enter address line two: ")
    pin_code = input("enter pincode: ")
    guardian_contact = input("enter parent's/guardian's contact number: ")

    print("\n" + schoolName.center(50))
    print(f"Student name: {name:<25} Roll No: {roll}")
    print(f"Class: {grade:<25} Section: {section}")
    print(f"Address: {addressOne}\n\t\t{addressTwo}")
    print("\nCity: {city:<32} Pin Code: {pin_code}")
    print(f"Parent's/Guardian's contact no: {guardian_contact}")

studentCard()