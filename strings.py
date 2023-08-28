# my_string ='G\'HRTcvb tutry'
# print(my_string)

# char= my_string[-3]
# print(char)

# # my_string[0]='h'

# substring= my_string[1:6]
# print(substring)

# name = "Ksu "
# sentence = name + " " + char
# print(sentence)

# for i in sentence:
#     print(i)


# if 't' in sentence:
#     print("yes")
# else:
#     print("no")

# myStr2 = '   Hello World   '
# myStr2 = myStr2.strip()
# print(myStr2)

# print(myStr2.lower())
# print(myStr2.startswith('H'))

# print(myStr2.find('o'))
# print(myStr2.count('l'))

# print(myStr2.replace('l', 'L'))


# my_list = myStr2.split()
# print(my_list)

# new_string=''.join(my_list)
# print(new_string)



# my_list = ['a'] *6
# print(my_list)

# from timeit import default_timer as timer
# # bad
# start = timer()
# my_string = ''
# for i in my_list:
#     my_string  += i
# print(my_string)
# stop=timer()
# print(stop-start)

# # good
# start = timer()
# my_string =''.join(my_list)
# print(my_string)
# stop=timer()
# print(stop-start)


# %, .format(), f-String

# var="Tom"
# Old
var = 6.653558
my_string="The variable is %.3f" % var   
print(my_string)

# New
var = 6.653558
var2 = 'Tre'
my_string="The variable is {:.4f} and {}".format(var, var2)
my_string1=f"The variable is {var*2} and {var2}"
print(my_string)
print(my_string1)