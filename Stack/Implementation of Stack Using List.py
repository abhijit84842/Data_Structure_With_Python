stack=[]

def push():
    element= int(input("Enter the number : "))
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty...")
    else:
        pop_item=stack.pop()
        print(f"Pop item is {pop_item}")
        print(stack)


while True:
    print("Plz select the operation which you want to perform 1.push , 2.pop  , 3.quit...")

    choice = int(input("Enter the operation number.. "))

    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice == 3:
        break
    else:
        print("Plz enter the correct operation number ..")