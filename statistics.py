import math
from turtle import st

def calculateStats(numbers):

  stats = dict(zip(["avg", "max", "min"], [math.nan, math.nan, math.nan]))

  if type(numbers) != list: 

    return None
    
  if len(numbers) != 0:

    stats["avg"] = round((sum(numbers) / len(numbers)), 3)
    stats["max"] = max(numbers)
    stats["min"] = min(numbers) # min_max_report test 
  
  return stats