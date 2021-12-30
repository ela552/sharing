languages = ["german", "english", "spanish", "rutooro", "luganda", "lusoga"]
print(languages[4])
print(languages[-2])

languages[1] = "french"
print(languages)

languages.append("greek")
print(languages)

del languages[0]
print(languages)

languages.pop()
print(languages)

languages.insert(2, "polish")
print(languages)

languages.remove("lusoga")
print(languages)

print(sorted(languages))
print(sorted(languages, reverse=True))

languages.reverse()
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(len(languages))