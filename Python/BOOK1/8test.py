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
