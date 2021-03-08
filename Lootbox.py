import random as r

for i in range(1000):
    x = open("Credits.txt", "r")
    credits = int(x.read())
    
    if credits < 100:
        print("You don't have enough credits!", "\n")
        print("You can buy more credits in the shop.")
        break
        
    credits -= 100
    credits = str(credits)
    x.close()
    
    y = open("Credits.txt", "w")
    edit = y.write(credits)
    y.close()
    
    lootbox_val = r.randrange(1,100) 
  
    if lootbox_val in range(1, 65):
        rarity = "Common"
        print(rarity)
    elif lootbox_val in range(65, 80):
        rarity = "Uncommon"
        print(rarity)
    elif lootbox_val in range(80, 91):
        rarity = "Rare"
        print(rarity)
    elif lootbox_val in range(91, 96):
        rarity = "Epic"
        print(rarity)
    elif lootbox_val in range(96, 99):
        rarity = "Mythic"
        print(rarity)
    elif lootbox_val == 99:
        rarity = "Legendary"
        print(rarity)
        
    z = open("Cards.txt", "a")
    edit = z.write(rarity + "\n")
    z.close()
     
    
    cont = input("Play again for 100 credits? (Y/N): ")
  
    if cont == "Y":
        continue
    elif cont == "N":
        break
    else:
        print("Invalid Input")
        continue