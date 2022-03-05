import math

def calculateStats(numbers):

  stats = dict.fromkeys(["avg", "max", "min"])


  if type(numbers) != list:

    return None # invalid_arg test


  if len(numbers) == 0:

    for key in stats.keys():
      
      stats[key] =  math.nan # is_nan test

  else:

    stats["avg"] = round((sum(numbers) / len(numbers)), 3)
    stats["max"] = max(numbers)
    stats["min"] = min(numbers) # min_max_report test 
  
  return stats
