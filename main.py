users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 1500000, },
    {"name": "Adrian", "surname": "Dobrzanski", "posts": 1, }

]
print("Informacje o Twoich znajomych: ")
for user in users:
    print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikował(a) {user["posts"]} postów')
