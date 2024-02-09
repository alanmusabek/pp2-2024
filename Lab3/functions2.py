movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def imdbScore(movie):
    for dictionary in movies:
        if(dictionary["name"] == movie):
            return dictionary["imdb"]


print(imdbScore("Detective"))

#2
def sublistFiveandAbove():
    sublist = []
    for dictionary in movies:
        i = 0
        if(dictionary["imdb"] > 5.5):
            sublist.append(dictionary["name"])
    return sublist

sublistOfMovies = sublistFiveandAbove()
for item in sublistOfMovies:
    print(item)

print(" ")
#3
def printCategories(category):
    for dictionary in movies:
        if(dictionary["category"]==category):
            print(dictionary["name"])

printCategories("Romance")

#4
list = ["The Choice", "Colonia", "Love", "Bride Wars", "We Two"]

def averageIMDBSCORE(listofMovies):
    sum = 0
    for item in listofMovies:
        for dictionary in movies:
            if(dictionary["name"] == item):
                sum += dictionary["imdb"]
    return sum / len(listofMovies)

print(averageIMDBSCORE(list))

#5

category = "Comedy"

def averageCategoryIMDBSCORE(category):
    sum = 0
    amount = 0
    for dictionary in movies:
        if(dictionary["category"] == category):
            sum += dictionary["imdb"]
            amount += 1
    return sum / amount

print(averageCategoryIMDBSCORE(category))
