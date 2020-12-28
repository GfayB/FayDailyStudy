#7.3.3使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")

    if repeat == 'no':
        polling_active = False
print("/n--- Poll request ---")
for name,repsonse in responses.items():
    print(name + " would like to climb " + response + ".")

#7-8
sandwich_orders = ['Beef Sandwich','Pork Sandwich','Tomato Sandwich']
print (sandwich_orders)
finished_sandwiches = []

while sandwich_orders:
    this_sandwich = sandwich_orders.pop()
    print("I made your "+ this_sandwich + '.')
    finished_sandwiches.append(this_sandwich)
print(finished_sandwiches)    
print("All sandwiches have been finished!")
