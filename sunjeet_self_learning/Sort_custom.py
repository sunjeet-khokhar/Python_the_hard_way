#bubble sort in Python
 
def bubble_sort(input_list):
  for x in range(0,len(input_list)-1,1):
    for i in range(0,len(input_list)-1,1):
      if input_list[i] > input_list[i+1]:
        temp = input_list[i]
        input_list[i] = input_list[i+1]
        input_list[i+1] = temp
  print(input_list)

  
l = [54,26,93,17,3,112,45,6,90,22,1,0,-3,444,1,0, 3, 4,222,5,34,62,-0,234]

bubble_sort(l)

      
   
   
 
        
        
    


