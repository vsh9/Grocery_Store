import random
print('''                                          100%Fresh
                Welcome to 100%Fresh,shop here and leave with the best''')
o=int(input('''enter 1 to get the items available in the store,enter 2 to look at the discounts'''))
while o==1 or o==2:
    if o==1:
        print('''
                           A)Dairy                     B)Fruits &Vegetables
                           1.Cheese  Rs.50per cube     1.Apple   Rs.200per kg
                           2.Milk    Rs.20per packet   2.Banana  Rs.100per kg 
                           3.Curd    Rs.15per packet   3.Tomato  Rs.35per kg
                           4.Ghee    Rs.55per packet   4.Carrot  Rs.80per kg

                           C)Snacks
                           1.Frozen nuggets         Rs.120per packet
                           2.Chips                  Rs.20per packet
                           3.Frozen Cheese balls    Rs.150per packet
                           4.Chocolate              Rs.30per bar

                           D)Toiletries
                           1.Harpic        Rs.200per bottle
                           2.Toothbrush    Rs.20per brush
                           3.Toothpaste    Rs.100per tube
                           4.Toilet paper  Rs.80per roll

                           E)Meat
                           1.Fish       Rs.500per kg
                           2.Chicken    Rs.200per kg
                           3.Pork       Rs.600per kg
                           4.Crab       Rs.350per kg''')
    elif o==2:
            print('''
             A)Dairy
              1.cheese 20% off if you buy 5 cubes
              2.ghee 10% off if you buy 2 packets
             B)Fruits and Vegetables
              1.Banana 15% off if you buy 6 kgs
              2. Carrot 25% off if you buy 4 kgs
             C)Snacks
              1.Frozen nuggets 5% off if you buy 2 packets
              2.Frozen cheese balls 10% off if you buy 3 packets
             D)Toiletries
              1.Harpic 20% off if you buy 2 bottils
              2.Toilet paper 15% off if you buy 3 rolls
              3.Buy 2 Toothpastes and get 1 dental floss free
             E)Meat
              1.Fish 15% off if you buy 3 kgs
              2.Chicken 30% off if you buy 2kgs''')
    else:
        print ("invalid input")
    del(o)
    o=int(input('''enter 1 to get the items available in the store,
enter 2 to look at the discounts
else enter any number to continue'''))
tot=0
x=('a','b','c','d','e')
while True:
    x=str(input('enter your category a,b,c,d,e:'))
    y=int(input("enter a product 1,2,3,4:"))
    z=int(input("enter required quantity:"))
    h=int(input("if you wish to delete entered quantity of the item please enter 3 else enter any number"))
    if h==3 :
        del(z)
        z=float(input("enter required quantity:"))
    p=int(input('''enter 5 to continue shopping or press any other number
to end shopping and get bill amount:'''))
    bill=0
    dis=0
    if p==5:
        continue
        if x=='a' and y==1 :
            if z==5:
                dis=20/100*z*50
                bill=z*50-dis
        elif x=='a' and y==2:
            bill=z*20
        elif x=='a' and y==3 :
            bill=z*15
        elif x=='a' and y==4:
            if z==2:
                dis=10/100*z*55
                bill=z*55-dis
        elif x=='b' and y==1 :
            bill=z*200
        elif x=='b' and y==2:
            if z==6:
                dis=15/100*z*100
                bill=z*100-dis
        elif x=='b' and y==3 :
            bill=z*35
        elif x=='b' and y==4:
            if z==4:
                dis=25/100*z*80
                bill=z*80-dis
        elif x=='c' and y==1 :
            if z==2:
                dis=5/100*z*120
                bill=z*120-dis
        elif x=='c' and y==2:
                bill=z*20
        elif x=='c' and y==3 :
            if z==3:
                dis=10/100*z*150
                bill=z*150-dis
        elif x=='c' and y==4:
            bill=z*30
        elif x=='d' and y==1 :
            if z==2:
                dis=20/100*z*200
                bill=z*200-dis
        elif x=='d' and y==2:
            bill=z*20
        elif x=='d' and y==3 :
            bill=z*100
        elif x=='d' and y==4:
            if z==3:
                dis=15/100*z*80
                bill=z*80-dis
        elif x=='e' and y==1 :
            if z==3:
                dis=15/100*z*500
                bill=z*500-dis
        elif x=='e' and y==2:
            if z==2: 
                dis=30/100*z*200
                bill=z*200-dis
        elif x=='e' and y==3 :
            bill=z*600
        elif x=='e' and y==4:
            bill=z*350
        elif x!=p:
            print("invalid input")
            break
        elif y>4:
            print("invalid input")
            break
        bill==n
    if tot==1000:
        disc=10/100*tot
        print("you have recieved a special discount of 10% on your total")
        tot=bill-disc
    elif tot>1000 and tot<=2000:
        disc=20/100*tot
        print("you have recieved a special discount of 20% on your total")
        tot=bill-disc
    elif tot>2000 and tot<=3000:
        disc=25/100*tot
        print("you have recieved a special discount of 25% on your total")
        tot=bill-disc
    elif tot>3000:
        disc=35/100*tot
        print("you have recieved a special discount of 35% on your total")
        tot=bill-disc
    if p!=5:
        i=0
        if x=='d' and y==3:
            if z%2==0:
                c=z+1
                for z in range(2,c,2):
                    b=z/2
                    i+=1
            elif z%2!=0:
                c=z
                z=z-1
                for a in range (2,c,2):
                    b=z/2
                    i+=1
            print("free item=dental floss,no. of items=",i)
        u=int(input("enter 1 for recyclable bag and 2 if you dont want a bag"))
        if u==1:
             b=input("enter small for small bag,medium for medium bag and big for a large bag")
             if b=='small':
                 tot=tot+5
                 print("carry bag=Rs.",5)
             elif b=='medium':
                 tot=tot+10
                 print("carry bag=Rs.",10)
             elif b=='big':
                 tot=tot+12
                 print("carry bag=Rs.",12)
        if tot>=2500:
            print('''Congrats you have won a chance to win a prize in
                     'The Random Draw',a game for all ages''')
            s=int(input("enter 1 to play else enter any number to get bill"))
            if s==1:
                q=random.choice([1,2,3,4,5])
                if q==1:
                    print ("You have won Rs.150")
                    tot=tot+150
                elif q==2:
                    print("You have won Rs.100")
                    tott=tot+100
                elif q==3:
                    print("You have won a gift coupon for some chocolates")
                elif q==4:
                    print("Luck dosent seem to be on your side today,try some other day")
                elif q==5:
                    print('''Today is your lucky day! You have won a hamper from dairy milk worth Rs.150''')
        f=input('''would you like a membership card!?''')
        if f=="yes":
            print('''thank you for choosing to be a member of our community
please enter your details in the form below and pay Rs.100 to register''')
            a=input("enter your name")
            b=int(input("enter your age"))
            c=int(input("enter your date of birth with '_' between the date,month,year"))
            tot=tot+100
        elif f=="no":
            d=input("do you already have a membership card?")
            if d=="yes":
                g=random.choice([10,20,30,40,50])
                if g==10:
                    tot=tot-10/100*tot
                    print("you're card has",g,"points therefore you have availed 10% discount")
                elif g==20:
                    tot=tot-20/100*tot
                    print("you're card has",g,"points therefore you have availed 20% discount")
                elif g==30:
                    tot=tot-30/100*tot
                    print("you're card has",g,"points therefore you have availed 30% discount")
                elif g==40:
                    tot=tot-40/100*tot
                    print("you're card has",g,"points therefore you have availed 40% discount")
                elif g==50:
                    tot=tot-50/100*tot
                    print("you're card has",g,"points therefore you have availed 50% discount")
            elif d=="no":
                print("thank you for your time")
        else:
            print("invalid input")
    print('''
                 Thank you for shopping at 100%Fresh,we hope to see you again''')
    print("Your original amount=Rs.=",bill)
    print("Your bill amount=Rs.",tot)
    break
