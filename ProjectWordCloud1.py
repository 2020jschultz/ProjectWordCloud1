#put pride and prejudice inside data_set
data_set = ""

split_it = data_set.split() 

Counter = Counter(split_it)

most_occur = Counter.most_common(1) 
  
print(most_occur)
