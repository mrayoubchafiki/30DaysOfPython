#DAY 5 OF 30DAYSOFPYTHON
#EXERCISE1
empty_list = []
list1 = ['orange', 'mango', 'lemon', 'kiwi', 'lime', 'apple']
print(len(list1))
first_item = list1[0]      
middle_item = list1[len(list1) // 2]
last_item = list1[-1]     
print(first_item, middle_item, last_item)

mixed_data_types = ['Jordan','25','175','married','California']
it_companies = ['Facebook', 'Google', 'Microsoft','Apple','IBM','Amazon']
print(it_companies)
print("Numbers of companies : ",len(it_companies))
print("The first company : ", it_companies[0])
print("The middle company : ", it_companies[len(it_companies)//2])
print("The last company : ", it_companies[-1])
it_companies[1] = 'AWS'
print(it_companies)
it_companies.append('Meta')
print(it_companies)
it_companies.insert(len(it_companies) // 2 ,"Oracle")
print(it_companies)
it_companies[2] = it_companies[2].upper()
print(it_companies)
result = '#;  '.join(it_companies)
print(result)
print('AWS' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse = True)
print(it_companies)

first_tree =  it_companies[0:3]
print(first_tree )
last_tree = it_companies[-3:]
print(last_tree)

middle_company = it_companies[len(it_companies)//2]
print(middle_company)

del it_companies[0]
print(it_companies)

del it_companies[len(it_companies)//2]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

del  it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
full_stack = join_list.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#EXERCISE2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("min : ", max(ages))
print("max : ", min(ages))
median = (ages[4] + ages[5]) / 2
print("Median : ",median)
average = sum(ages) / len(ages)
print("Average : ",average)
range_age = max(ages) - min(ages)
print(range_age)
print(abs(min(ages) - average) < abs (max(ages)- average))


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
mid_index = (len(countries) + 1) // 2
first_half = countries[:mid_index]
second_half = countries[mid_index:]
print("First half : ",first_half)
print("Second half : ",second_half)

list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
county1,country2,country3,*scandic = list
print("first tree : ",county1,country2,country3)
print("scandic countries : ", scandic)

