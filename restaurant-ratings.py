#We have to import the file
#Turn it into a dict
#Use sorted() dict in for statement

restaurant_scores = open('scores.txt')
restaurant_ratings = {}

for line in restaurant_scores:
    line = line.rstrip()
    restaurant_data = line.split(":")

    restaurant_ratings[restaurant_data[0]] = restaurant_data[1]

for restaurant, rating in sorted(restaurant_ratings.items()):
    print '{} is rated at {}.'.format(restaurant, rating)

