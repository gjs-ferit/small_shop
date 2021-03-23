#python 3

import copy

items_dict = {} #dictionary for items, keys are sku numbers , values are dictionaries with key - value pairs for name, quantity and price
shopping_cart = {}
count = 1 #counter for stages of process 
while (count == 1) :
    std_inp = input('STDIN: ')
    std_inp_split = std_inp.split()
    if (std_inp_split[0] == 'ADD'):
         items_dict[std_inp_split[1]] = {'name' : std_inp_split[2],      
        'quantity' : int(std_inp_split[3]),        
        'price' : float(std_inp_split[4])  }

    elif(std_inp == 'END'):
        count = count + 1

while (count == 2) : 
    std_inp = input('STDIN: ')
    std_inp_split = std_inp.split() #spliting original input into separate strings in a list, enabling to access to wanted value by index 
    
    if (std_inp_split[0] == 'ADD'): #ADD
        shopping_cart[std_inp_split[1]] = copy.deepcopy(items_dict[std_inp_split[1]]) #deepcopying to avoid manipulating both dictionaries when removing items from inventory
        shopping_cart[std_inp_split[1]]['quantity'] = int(std_inp_split[2]) #access third value in STDIN, converting it to int and putting it as value for 'quantity' key for item we want to add in basket
        items_dict[std_inp_split[1]]['quantity'] = items_dict[std_inp_split[1]]['quantity'] - int(std_inp_split[2]) #removes same number of items from inventory as user puts in basket 

        
    elif (std_inp_split[0] == 'REMOVE'): #REMOVE
        shopping_cart[std_inp_split[1]]['quantity'] = shopping_cart[std_inp_split[1]]['quantity'] - int(std_inp_split[2])
        items_dict[std_inp_split[1]]['quantity'] = items_dict[std_inp_split[1]]['quantity'] + int(std_inp_split[2]) #adds same number of items to inventory as user removes from basket 


    elif (std_inp_split[0] == 'CHECKOUT'): #CHECKOUT
        total = 0
        for item in shopping_cart:
            print(shopping_cart[item]['name'] + ' ' + str(shopping_cart[item]['quantity']) + ' x ' + str(shopping_cart[item]['price']) + ' = ' + 
            str(round((shopping_cart[item]['quantity']*shopping_cart[item]['price']), 2))) #prints string with product name, quantity in basket, price per item, and total for this product rounded to 2 decimal points
            total = total + shopping_cart[item]['quantity']*shopping_cart[item]['price'] 
        print('TOTAL = ' + str(round(total, 2)))
        shopping_cart = {}

    elif (std_inp_split[0] == 'END'): #END
        count = count + 1
