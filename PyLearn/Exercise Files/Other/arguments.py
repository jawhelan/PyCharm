
def my_funtion(*args, **kwargs):
  print (kwargs)

my_funtion (12, a=17, b="boy")


# there are two related concepts, both called "keyword arguments".

# On the calling side, which is what other commenters have mentioned, you have the ability to specify some function arguments by name. You have to mention them after all of the arguments without names (positional arguments), and there must be default values for any parameters which were not mentioned at all.

# The other concept is on the function definition side: You can define a function that takes parameters by name -- and you don't even have to specify what those names are. These are pure keyword arguments, and can't be passed positionally. The syntax is

# def my_function(arg1, arg2, **kwargs)
# Any keyword arguments you pass into this function will be placed into a dictionary named kwargs. You can examine the keys of this dictionary at run-time, like this:

# def my_function(**kwargs):
  #  print str(kwargs)

#my_function(a=12, b="abc")

# {'a': 12, 'b': 'abc'}


