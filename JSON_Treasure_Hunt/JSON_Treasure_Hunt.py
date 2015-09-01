import json

json_obj1 = json.load(open("text1.txt"))
json_obj2 = json.load(open("text2.txt"))

#print(json.dumps(json_obj1, indent=1))
#print(json_obj1)
word = 'dailyprogrammer'
map = []

test_obj = {'a':'dailyprogrammer','b':3}

def find_word(obj, word, map):
    """ This is a recursive function """
    #return word in obj - searches the keys
    #return word in obj - searches the values

    

print(find_word(test_obj, 'a'))
