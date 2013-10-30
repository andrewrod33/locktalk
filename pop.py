fizz = ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, 100)]
print fizz

#def insertion_sort(list):
#    for index in range(1, len(list)):
#        value = list[index]
#        i = index - 1
#        while i>=0:
#            if value < list[i]:
#                list[i+1] = list[i]
#                list [i] = value
#                i = i -1
#            else:
#                break
#numbers = [4, 1, 2, 3]
#insertion_sort(numbers)
#print numbers

