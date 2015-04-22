full_name = "james Whelan"
# split full name "James Whale" into "James", "whelan"
name_list = full_name.split()
greeting_var="hello my name is tim"
#split string "hello my name is tim" to "hello", "my"," name", "is", "tim"
greeting_list = greeting_var.split()
# swap out the name tim with james
greeting_list[4] = name_list[0]
# join the split string back into one varable
greeting_list = " ".join(greeting_list)
print(greeting_list)