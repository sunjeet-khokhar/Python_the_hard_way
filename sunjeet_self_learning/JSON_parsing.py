# parse the JSON dict below and print the value of the key 'id1'
# source --> https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
#output should be -> 'blabla1'

import json
#import pprint

json_dict = {
    "maps": [
        {
            "id1": "blabla1",
            "iscategorical": "0"
        },
        {
            "id2": "blabla2",
            "iscategorical": "10"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}

map_list = json_dict['maps']
print(map_list[0]['id'])