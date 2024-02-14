  1 import random
  2 
  3 crafts_num = int(input("How many space crafts do you wish? "))
  4 
  5 while crafts_num < 2 or crafts_num > 10:
  6         crafts_num = int(input("Please, follow the range of 2 to 10: "))
  7         
  8 def create_spacecrafts(crafts_num):
  9         """
 10         Creates a dictionary that will contain 'crafts_num' of spacecrafts ob
    jects with unique names.
 11         Args: 
 12             crafts_num: total crafts to make
 13 
 14         Returns:
 15             a dictionary where keys are unique spaceship names (based on lett    er in lowercase plus its names)    
 16         """
 17        
