
# nesting multiple dictionaries and a list , with in a dictionary
music_dict_nested_list = {'Thelonious Monk' : 
                            {  'Country' :  'America' , 'Available_albums' : [{'album_name' : 'Round Midnight','year' :'1998'}, {'album_name' : 'The best years','year' :'1963'}]
                              , 'Genre' : 'Jazz' 
                             }
                            ,'Antonio Carlos Jobim':
                            {  'Country' :  'Brazil' , 'Available_albums' : [{'album_name' : 'Amore','year' :'1959'}, {'album_name' : 'The blue stand','year' :'1972'}]
                              , 'Genre' : 'Blues'                              
                            }
                            }

#function that accepts the artist_name and prints their available albums in the store 
def retrieve_artist_albums(artist_name):
    # get the list that holds dictionaries that contrain album names and year of release
    list1 = music_dict_nested_list[artist_name]['Available_albums']
    #iterate through the list and print each key and value of the dictionaries contained in them
    for item in list1:
        for key in item:
            # oops this does not print in a single line , i need to look into this !
            print(artist_name,key,item[key])
           #clean_dict = {key.strip('{'): item.strip('{') for key, item in item.items()}
    

#function being called with artists name 
retrieve_artist_albums('Thelonious Monk')
retrieve_artist_albums('Antonio Carlos Jobim')

	

