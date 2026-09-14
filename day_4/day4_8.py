Thirty = 'Thirty'
Days = 'Days'
Of = 'Of'
Python = 'Python'
fullsentence = Thirty + ' ' + Days + ' ' + Of + ' ' + Python
print(fullsentence)

Coding = 'Coding'
For = 'For'
All = 'All'
fullsentence2 = Coding + ' ' + For + ' ' + All
print(fullsentence2)

Company = 'Coding For All'
print(Company)
print("length of company is ",len(Company))
print(Company.upper())
print(Company.lower())
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())

first_word = Company[0:6]
print(first_word)

print(Company.find('Coding'))
print(Company.replace('Coding','Python'))
print(Company.split())

s = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s.split( ', '))

print(Company[0])
last_index = len(Company) - 1
print(Company[last_index])
print(Company[10])

text1 = "Python For Everyone"
acronym1 = text1[0] + text1[7] + text1[11]
print(acronym1)
text2 = "Coding For All"
acronym2 = text2[0] +  text2[7] +  text2[11]
print(acronym2)

print(text2.index("C"))
print(text2.index("F"))
print(text2.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))
print(sentence.rindex("because"))
print(sentence[31:55])

print(text2.startswith('Coding'))
print(text2.endswith('coding'))

text3 = '   Coding For All      '  
print(text3.strip())

x = '30DaysOfPython'
y = 'thirty_days_of_python'
print(x.isidentifier())
print(y.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(libraries)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(raduis,area))

x=8
y=6
print("{} + {} = {}".format(x,y,x+y))
print("{} - {} = {}".format(x,y,x-y)) 
print("{} * {} = {}".format(x,y,x*y))
print("{} / {} = {}".format(x,y,x/y))
print("{} % {} = {}".format(x,y,x%y))
print("{} // {} = {} ".format(x,y,x//y))
print("{} ** {} = {}".format(x,y,x**y))
