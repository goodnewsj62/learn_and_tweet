#suppose  you have a sequence like so
x =  (1,"a", "b", "c",4)

#and you want to grab just the first and last item 
# since they are digit... a simple way to do that is 
#by destructring with the * operator like so

a, *b ,c =  x

print(a,c, sep=",")
#RESULT: 1,4
# from the result a is assigned the first item on the list
# while c is assigned the last item


#the remaining items on the list is assigned to b because
#of the * operator
print(b)
#RESULT: ['a', 'b', 'c']

#incase you do not need b you could use _ to replace b
# as the variable like so

a, *_,  b =  x