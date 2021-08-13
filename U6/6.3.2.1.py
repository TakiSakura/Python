favorite_languages= dict(jen='python', sarah='c', edward='ruby', phil='python')
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi {0},I see your favorite language is {1}!".format(name.title(), favorite_languages[name].title()))