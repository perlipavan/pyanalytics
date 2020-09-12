My_string_1 = 'hi'
My_string_2 = "yo"

#""""""" lets you go beyond a line
my_strings = """hello                                                            ji    """

print(my_strings)

num_x = None
print(num_x is None)

#Boolean types - True, False

x = str(4.0)
print(type(x))

#Dictionary starts with curly braces
#Key:Value, Key is immutable, value is mutable
#you cannot perform calculations on keys and better keep them string value
my_first_dictionary = {"A":1,"B":2}
print(my_first_dictionary)
print(my_first_dictionary.values())
print(my_first_dictionary.keys())

print(my_first_dictionary["A"])

my_first_dictionary.update({"A":[0,1]})
print(my_first_dictionary)

#set
auto_survey = set(['Audi', 'Benz', 'BMW'])
print(auto_survey)

My_first_set= {'GM','Audi','Mercedes'}
print(My_first_set)
#union
print(My_first_set|auto_survey)

#intersection
print( My_first_set&auto_survey)

null_value = 'Hello'
print(null_value is None)

Boolean_value = True

#Adding tuples
test_score_1 = (12,14,15)
test_score_2 = (13,16)

test_score = test_score_1 + test_score_2
print(test_score)

test_score_multiplied = test_score_1 * 5
print(test_score_multiplied)

print(My_string_1 * 5)

first_line = [34,45,0, None, True, "Green", (23,45,67.0)]
print('ree' in first_line[5])

#Functions are the primary method of code organization and reuse in python
