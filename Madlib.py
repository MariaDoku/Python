#madlibs!
# string concatenation (aka how we put strings together)
# if we want to make a string that says "My favorite architecture style is _______"
#myfavstyle = "modern" # some string variable

#here's a few methods we can take to do this
#print("My favorite architecture style is " + myfavstyle)
#print("My favorite architecture style is {}".format(myfavstyle))
#print(f"My favorite architecture style is {myfavstyle}") #F string looks cleanest right?

#lets use the F String for this project

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Your Favorite Designer: ")

madlib = f"Architecture is very {adj}! Computational design is especially fun because \
I love to {verb1}. Work hard and {verb2} just like {famous_person}!"

print (madlib)