def my_menu(my_options, selected_index):
    for i, option in enumerate(my_options):
        if i == selected_index:
            print (" [*] {}".format(option))
        else:
            print (" [ ] {}".format(option))

my_options = ['Option 0', 'Option 1', 'Option 2', 'Option 3']
my_menu(my_options, 1)
