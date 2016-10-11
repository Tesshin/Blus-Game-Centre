import random

# Game 1 statistics in 2014
# http://www.movehub.com/blog/popular-countries-map
game1_countries = ['France', 'United States', 'China', 'Spain', 'Italy',
                   'Turkey', 'United Kingdom', 'Germany', 'Russian Federation', 'Malaysia',
                   'Mexico', 'Austria', 'Hong Kong', 'Ukraine', 'Thailand',
                   'Saudi Arabia', 'Greece', 'Canada', 'Poland', 'Macao',
                   'Netherlands', 'Singapore', 'Hungary', 'Croatia', 'Korea',
                   'Egypt', 'Morocco', 'Czech Republic', 'Switzerland', 'South Africa',
                   'Indonesia', 'Ireland', 'Romania', 'Belgium', 'Denmark',
                   'Portugal', 'Bahrain', 'Bulgaria', 'India', 'Japan',
                   'Vietnam', 'Australia', 'Argentina', 'Brazil', 'Sweden',
                   'Norway', 'Tunisia', 'Dominican Republic', 'Finland', 'Jordan']

game1_popularity = ['81,400,000', '62,700,000', '57,600,000', '56,700,000', '46,100,000',
              '34,000,000', '29,300,000', '28,400,000', '24,900,000', '24,700,000',
              '23,400,000', '23,000,000', '22,300,000', '21,400,000', '19,200,000',
              '17,500,000', '16,400,000', '16,000,000', '13,400,000', '12,900,000',
              '11,300,000', '10,400,000', '10,300,000', '9,900,000', '9,800,000',
              '9,500,000', '9,300,000', '8,800,000', '8,500,000', '8,300,000',
              '7,700,000', '7,600,000', '7,600,000', '7,500,000', '7,400,000',
              '7,300,000', '6,700,000', '6,300,000', '6,300,000', '6,200,000',
              '6,000,000', '5,900,000', '5,700,000', '5,400,000', '5,000,000',
              '5,000,000', '4,800,000', '4,300,000', '4,200,000', '4,000,00']

# Game 2 statistics in 2015
# http://www.infoplease.com/world/statistics/most-populous-countries.html
game2_countries = ['1,367,485,388','1,251,695,584', '321,368,864', '255,993,674', '204,259,812',
                   '199,085,847', '181,562,056', '168,957,745', '142,423,773', '126,919,659',
                   '121,736,809', '100,998,376', '99,465,819', '94,348,835', '88,487,396',
                   '81,824,270', '80,854,408', '79,414,269', '79,375,136', '67,976,405',
                   '66,553,766', '64,088,222', '61,855,120', '56,320,206', '53,675,563',
                   '51,045,882', '49,115,196', '48,146,134', '46,736,728', '45,925,301',
                   '44,429,471', '43,431,886', '39,542,166', '38,562,189', '37,101,745',
                   '37,056,169', '36,108,853', '35,099,836', '35,099,836', '32,564,342',
                   '31,551,305', '30,513,848', '30,444,999', '29,275,460', '29,199,942',
                   '27,752,316', '26,737,317', '26,327,649', '25,303,113', '24,983,205']

game2_population = ['China ', 'India ', 'United States ', 'Indonesia ', 'Brazil ',
                    'Pakistan ', 'Nigeria ', 'Bangladesh ', 'Russia ', 'Japan ',
                    'Mexico ', 'Philippines ', 'Ethiopia ', 'Vietnam ', 'Egypt ',
                    'Iran ', 'Germany ', 'Turkey ', 'Democratic Republic of Congo ', 'Thailand ',
                    'France ', 'United Kingdom ', 'Italy ', 'Burma ', 'South Africa ',
                    'Tanzania ', 'Korea', 'South ', 'Spain ', 'Colombia ',
                    'Kenya ', 'Ukraine ', 'Argentina ', 'Algeria ', 'Poland ',
                    'Uganda ', 'Iraq ', 'Sudan ', 'Canada ', 'Morocco ',
                    'Afghanistan ', 'Nepal ', 'Malaysia ', 'Peru ', 'Venezuela ',
                    'Uzbekistan ', 'Saudi Arabia ', 'Yemen ', 'Ghana ', 'Mozambique ', 'North Korea']

print("How many")

# Game 3 United States Capital Cities
# http://www.infoplease.com/ipa/A0763765.html
game3_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
                "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
                "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

game3_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento",
                  "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta",
                  "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines",
                  "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis",
                  "Boston", "Lansing", "St. Paul", "Jackson", "Jefferson City",
                  "Helena", "Lincoln", "Carson City", "Concord", "Trenton",
                  "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus",
                  "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia",
                  "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier",
                  "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

# TODO Start writing code