def beerDataGenerator():
    file = "data/recipeData.csv"
    for row in open(file, encoding="ISO-8859-1"):
        yield row

def testLC():
    lc = [n**2 for n in [1, 2, 3, 4, 5]]
    return lc

def generatorToDicts():
    file = "data/recipeData.csv"
    lines = (line for line in open(file, encoding="ISO-8859-1"))
    lists = (l.split(",") for l in lines)

    # Store to next in generators
    columns = next(lists)

    # Take these columns and use them to create an informative dictionary
    beerdicts = (dict(zip(columns, data)) for data in lists)
    print(beerdicts)
    return beerdicts


def mostoPopuraaBiiru(beerdicts):
    beer_counts={}
    for bd in beerdicts:
        if bd["Style"] not in beer_counts:
            beer_counts[bd["Style"]] = 1
        else:
            beer_counts[bd["Style"]] += 1
    
    most_popular = 0
    most_popular_type = None
    for beer, count in beer_counts.items():
        if count > most_popular:
            most_popular = count
            most_popular_type = beer
    
    return most_popular_type