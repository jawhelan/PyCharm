'''
Created on Apr 20, 2015

@author: james
'''
full_name = "james whelan"
name_list = full_name.split() #splits the name list into word list on white spaces
greeting_list ="Hi, I'm Treehouse".split()
greeting_list[2] = name_list[0]  # swap out the third word in greeting_list with the first word on name_list
                  
print(greeting_list)

print (" ".join(greeting_list))