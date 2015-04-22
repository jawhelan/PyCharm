
my_list = [1, 2.5,'a']
print( my_list[2])
print(len(my_list))
my_list[2]= 'b'
print (type(my_list),my_list)
my_str = list('hello',) #a string list
print(len(my_str), type(my_str),my_str)
my_sentence = " I'm a lumberjack an I'm ok I sleep all night and work all day"
print(my_sentence)
print(my_sentence.split()) # the .split sting function splits on string on white spaces
sentence_list = my_sentence.split() # setting the split sentence back into a list but split
print(' '.join(sentence_list)) # here the ' ' joins the string list back together,  whatever you put in the ' ' will be in the join

