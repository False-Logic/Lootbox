for i in range(1000):
    x = open("Credits.txt", "r")
    credits = int(x.read())
    print("\n")
    print("You have", credits, "credits.", "\n")
    
    try:
        credits_amount = int(input("How many credits would you like to buy?: "))
    except ValueError:
        print("\n", "Invalid Input")
        continue
    
    money = format(credits_amount / 100, ".2f")
    print("\n")
    print("This will cost $", end = "")
    print(money, "\n")
    
    confirm = input("Confirm your purchase? (Y/N): ")
    
    if confirm == "Y":
        print("\n")
        print("Confirmed!", "\n")
        print("A transaction of", "$", end = "")
        print(money, "has been charged to your account.", "\n")
        
    elif confirm == "N":
        print("\n")
        print("Transaction Canceled Sucessfully!", "\n")
        
        cont = input("Do you still want to purchase credits? (Y/N): ")
        if cont == "Y":
            continue
        elif cont == "N":
            break
        else:
            print("\n")
            print("Invalid Input")
            continue
           
    credits += credits_amount
    credits = str(credits)
    x.close()
    
    y = open("Credits.txt", "w")
    edit = y.write(credits)
    y.close()
    
    print(credits_amount, "credits have been added to your account, bringing your total balance to", credits, "credits", end = "") 
    print(".", "\n")
    
    cont = input("Would you like to buy more credits? (Y/N): ")
  
    if cont == "Y":
        continue
    elif cont == "N":
        break
    else:
        print("Invalid Input")
        continue