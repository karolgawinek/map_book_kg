def read_friends(users: list)->None:
    print("Informacje o Twoich znajomych: ")
    for user in users:
        print(f'\tTwoj znajomy {user["name"]} {user["surname"]} opublikował(a) {user["posts"]} postów')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbe postow uzytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, }
    lista.append(new_user)