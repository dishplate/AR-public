#decimal to unicode converter for picoCTF
# Python3 code to demonstrate
# Convert String list to ascii values
# using chr()
#Found the issue - the spaces are tabs! and they are not being removed by strip() for some reason.


#nums = ("55 25")
#print(nums)
#print(chr(110))



 # 112  105  99  111  67  84  70  123  103  48  48  100  95  107  49  116  116  121  33  95  110  49  99  51  95  107  49  116  116  121  33  95  102  50  100  55  99  97  102  97  125  10
nums = "112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 102 50 100 55 99 97 102 97 125 10"
x = nums.replace(' ', ',')
y = x.split(',')
# print(y)
# print("\n")
#z = [type(y)]
#print (z)

# x = nums.replace("'","")
# y = nums.replace("'",'')
#numint = [y]  # was able to change sting to list
#print(type(numint))
#print(numint)
#print(type(numint))
#print(chr((numint))) # need this to be int and not list

#print(nums)
list1 = []
for i in y:   #iterate through the string nums and turn it into a list
    list1.append(int(i))   #convert to integer as needed by chr()
#print(type(list1))
ints = list1

#print(ints) #print ints
# list2 =[]
# for a in ints:
#     print((chr(a))) #this line works, just need to make it horizontal
    #print(list2)
    #list2.append(chr(a))
    #print(list2)
    #print(list2.replace("'","")
flag = ""  #assign empty string
for number in ints:
    flag += chr(number)
print(flag)