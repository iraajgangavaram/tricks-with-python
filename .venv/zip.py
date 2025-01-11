#Use ZIP when working with lists
#Suppose you were given a task to combine several lists with the same length and print out the result? Again, here is a more generic way to get the desired result by utilizing zip() as shown in the code below:
countries = ['France', 'Germany', 'Canada']
capitals = ['Paris', 'Berlin', 'Ottawa']
for country, capital in zip(countries,capitals):
    print(country, capital)
