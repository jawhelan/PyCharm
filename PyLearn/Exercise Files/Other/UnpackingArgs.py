def health_calculator (age, apples, cigs_smoked):
    answer = (100-age) + (apples*2) - (cigs_smoked *2)
    print(answer)


my_info = [45, 20, 10]

health_calculator(my_info[0],my_info[1],my_info[2])  # the long way to unpack the table full of args

health_calculator(*my_info)        # the short wat to unpack a list of args