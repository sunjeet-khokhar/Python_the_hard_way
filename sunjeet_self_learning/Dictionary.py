#count the number of times a word appears in a string 

name = '''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked? '''

#this will split the sentence based on whatever is passed on as the argument , a blank space in this case and return a list
name_split = name.split(" ")

dict_words = dict()
for i in name_split:
    if i.isalnum():
        if i in dict_words:
            dict_words[i] = dict_words[i]+1
        else:
            dict_words[i] = 1

for key in dict_words.keys():
    print(f"The word \"{key}\" occurs {dict_words[key]} times")


#nested dictionary 

music_dict = { 'Composer' : 'Ustad Bade Ghulam Ali Khan' , 'House' : 'Undivided North India' , 'Specialization' : 'Thumri' }

#print(music_dict)



music_dict_nested = { 'Composer' : 'Ustad Bade Ghulam Ali Khan' , 'House' : { 'Location' : 'Undivided north India' , 'Era' : 'The golden age' , 'Primary_disciple' : 'Ustad Phanne Khan' } , 'Specialization' : 'Thumri'  }

# extract and print all the values in House dictionary

music_dict_nested_house = {}
music_dict_nested_house = music_dict_nested['House']

for item in music_dict_nested_house.values():
    print(item)

#or another shorter way is 

for item in (music_dict_nested['House'].values()):
    print(item)

# nesting a list within a dicitonary


music_dict_nested_list = { 'Composer' : 'Ustad Bade Ghulam Ali Khan' , 'Greatest_hits' : ['Bhor bhayee', 'Raag Bharavi' ] , 'Specialization' : 'Thumri' }
print(music_dict_nested_list['Greatest_hits'][1])


cities = {
    'CA': ['San Francisco','Los Angeles'],
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print(f"California has these cities --> {cities['CA']} ")
print(cities['CA'][0])

# nesting multiple dictionaries within a list
music_dict_nested_list_1 = {'Ustad Bade Ghulam Ali Khan' : 
                            { 'House' : 'The great undivided Punjab' , 'Country' :  'The great divided north' , 'Available_albums' : [{'album_name' : 'Naa aaye piya','year' :'1952'}, {'album_name' : 'Gujri todi','year' :'1963'}]
                             , 'Genre' : 'Thumri' 
                             }
                            ,'Ustad Ghulam Mustafa Khan':
                            { 'House' : 'Deccan Plateau' , 'Country' :  'The Deccan Herald' , 'Available_albums' : [{'album_name' : 'Raag Deepak','year' :'1959'}, {'album_name' : 'Piya ka malhaar','year' :'1972'}]
                            , 'Genre' : 'Alaap'                              
                            }
                           }


# print Available albums for Ghulam Mustafa Khan
print(music_dict_nested_list_1['Ustad Ghulam Mustafa Khan']['Available_albums'])
# now use the .get() method to return the value of a specific key e.g. return all the albums of Ustad GHulam Ali Khan
print(music_dict_nested_list_1.get('Ustad Ghulam Mustafa Khan'))





    
     

     

