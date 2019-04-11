
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError
   max_int = None
   for i in range(len(int_list)):
       if i == 0 or int_list[i] > max_int:
           max_int = int_list[i]

   return max_int

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError
   length = len(int_list)
   if length <= 0:
       return int_list
   return int_list[length - 1:] + reverse_rec(int_list[:length - 1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
       raise ValueError
   length = len(int_list)
   if length <= 0:
       return None

   middle = ((high + low) // 2)
   vals = [int_list[low], int_list[middle], int_list[high]]
   if target in vals:
       return [low, middle, high][vals.index(target)]

   if ((high - low) / 2) <= 1 or target > int_list[high] or target < int_list[low]:
       return None


   else:
       if target > int_list[middle]:
           return bin_search(target, middle, high, int_list)
       else:
           return bin_search(target, low, middle, int_list)
