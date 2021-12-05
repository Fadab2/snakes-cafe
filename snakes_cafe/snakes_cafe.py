
def menu_display():
    intro_message = '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    '''

    prompt = '''
    ***********************************
    ** What would you like to order? **
    ***********************************
    '''

    print(f'{intro_message} {prompt}')


menu = [
    {
    "name": "appetizers",
    "item": [
        "Wings",
        "Cookies",
        "Spring Rolls",
    ],
    },
    {
        "name": "entrees",
        "item": [
        "Salmon",
        "Steak",
        "Meat Tornado",
        "A Literal Garden",
    ],
    },
    
    {
    "name": "desserts",
    "item": [
        "Ice Cream",
        "Cake",
        "Pie"
    ],
    },
    {
    "name": "drinks",
    "item": [
        "Coffee",
        "Tea",
        "Unicorn Tears",
    ],
    },
]



if __name__== "__main__":
    menu_display()
    ordered_items = []
    item_count = 0
    user_input = ""
    
    while user_input != "quit": 
         
         user_input = input('> ')
         ordered_items.append(user_input)
         item_count = ordered_items.count(user_input)
         
         if (user_input in ordered_items) and item_count == 1:
            #  item_count = ordered_items(user_input)
             
             print(f'** {item_count} order of  {user_input} have been added to your meal **')
         elif item_count > 1:
            print(f'** {item_count} orders of  {user_input} have been added to your meal **')
        
         
#print(ordered_items)


