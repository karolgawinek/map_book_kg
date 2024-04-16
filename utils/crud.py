def read_friends(users: list)->None:
    print("Informacje o Twoich znajomych: ")
    for user in users:
        print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikował(a) {user["posts"]} postów')
