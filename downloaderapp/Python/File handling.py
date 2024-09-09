file = open("text.txt","x") 
    
with open("text.txt","w") as file:
    file.write(input("Enter your string: "))
    
with open("test.txt",'r') as file:
    print(file.read())