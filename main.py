MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash" : 10
}

def generate_report():
  print('\nResources: ' + str(resources) + '\n')

def process_order(selection):
  # Determine if there are enough resources
  water_needed = MENU[selection]['ingredients']['water']
  try:
    milk_needed = MENU[selection]['ingredients']['milk']
  except:
    milk_needed = 0
  coffee_needed = MENU[selection]['ingredients']['coffee']
  item_cost = MENU[selection]['cost']
  processed_tender = 0.0
  required_resources = True
  if(resources['water'] < water_needed):
    print('There is not enough water to process this order\n')
    required_resources = False
  if(resources['milk'] < milk_needed):
    print('There is not enough milk to process this order\n')
    required_resources = False
  if(resources['coffee'] < coffee_needed):
    print('There is not enough coffee to process this order\n')
    required_resources = False

  if(not required_resources):
    return
    
  # Take Payment
  print(f'\nThe item cost is {item_cost}. \nPlease insert coins\n')
  while(processed_tender < item_cost):
    payment = input('Remaining balance = ' + str(item_cost - processed_tender) + 
      '\n')
    processed_tender += float(payment)
  # Refund Overpayment
  if(processed_tender > item_cost):
    refund = processed_tender - item_cost
    print(f'Issuing refund of: {refund:.2f} ')
  
  # Modify resources #
  resources['water'] -= water_needed
  resources['milk'] -= milk_needed
  resources['coffee'] -= coffee_needed
  resources['cash'] += item_cost
  # Make Drink 
  print(f'Here is your {selection}!\n\n')

def Begin():
  machine_on = True
  while(machine_on):
    valid_choice = False
    while(not valid_choice):
      selection = input('Pick one: espresso, latte, cappuccino \n')
      if(selection == 'espresso' or selection == 'latte' or selection ==   
      'cappuccino'):
        valid_choice = True
      elif (selection == 'off'):
        machine_on = False
        while(not machine_on):
          turn_on = input('Machine is off. Hit enter to turn on.\n')
          machine_on = True
      elif(selection == 'report'):
        generate_report()
      else:
        print('Invalid selection. Try again.')
  
    process_order(selection)
    
Begin()
  