#8-1
def display_message():
    print("Study how to define a function and use it!")

display_message()

#8-2
def favorite_movie(title):
    print("One of my favorite movie is "+ title + ".")

favorite_movie("《Call me by your name》")

#8.2.1
def describe_pet(animal_type,pet_name):
    print ("I have a "+ animal_type + ",and I call it " + pet_name +"!")

describe_pet("dog","coder")
describe_pet("cat","milk")

#8.2.2
def describe_pet(animal_type,pet_name):
    print ("I have a "+ animal_type + ",and I call it " + pet_name +"!")

describe_pet(animal_type = "dog",pet_name = "coder")
describe_pet(animal_type = "cat",pet_name = "milk")   

#8.2.3
def describe_pet(pet_name,pet_age,animal_type = 'dog'):
    print ("I have a "+ animal_type + ",and I call it " + pet_name +"! It's " + str(pet_age) + " this year!")
#仅指定未设置默认值的参数,使用位置实参
describe_pet('coder',3)

#仅指定未设置默认值的参数，使用关键词实参
describe_pet(pet_age = 5,pet_name = 'milly')

#重新指定所有参数的值
describe_pet(pet_age = 4,pet_name = 'micky',animal_type = 'cat')

#8.3.1
def get_formatted_name (first_name,last_name):
    full_name = first_name +' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#将实参变为可选的
#给选填的middle_name设置一个默认值：空字符串
def get_formatted_name(first_name,last_name,middle_name = ''):
    #使用if语句判定后续是否给middle_name赋值
    if middle_name:
        full_name = first_name +' '+ middle_name +' '+ last_name
    else:
        full_name = first_name +' '+ last_name
    return full_name.title()

musician1 =get_formatted_name('jimi','hendrix')
musician2 =get_formatted_name('john','kooker','lee')
print (musician1)
print (musician2

       
       #8.3.4 函数和while的结合使用
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " +last_name
    return full_name.title()

while True:
    print ("\nPlease tell me your name:")
    print ("(Enter 'q' if you want to quit!)")

    f_name = input("Please insert your first name:")
    if f_name == 'q':
        break
    l_name = input ("Please insert your last name:")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello,"+formatted_name + "!")
