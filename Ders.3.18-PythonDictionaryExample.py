students={}

number=int(input("Enter A Student Number Please...: "))
name=input("Enter A Student Name Please...: ")
surname=input("Enter Student's Surname Please...: ")
phone=input("Enter Student's Phone Number Please...: ")


students[number]={
    "name":name,
    "surname":surname,
    "phone":phone
}

print(students)