## format()
# The format method the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curlybrackets:{}.


# named_indexes
t1 = "welcome to {name} {details}".format(name="Python", details='Course')
# numbered_indexes
t2 = "Welcome to {0} {1}".format("Python", "Course")
# empty_placeholder
t3 = "Welcome to {} {}".format("Python", "Course")
print(t1)
print(t2)
print(t3)


