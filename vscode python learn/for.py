favorite_languages = {
    'jens' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("the following languages have been mentions :")

for language in set(favorite_languages.values()):
    print(language.title())