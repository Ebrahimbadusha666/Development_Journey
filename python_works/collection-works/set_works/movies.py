

"""
def add(self,others) - to add set to existing set

def update(self,others) - to update set to set

"""

tamil_movies={"coolie","thuppaki","kakkamuttai"}

movies={"arm","lokah","kgf","kanthara"}

# movies.update(tamil_movies)

# print(movies)

all_movies=movies.union(tamil_movies)

print(all_movies)