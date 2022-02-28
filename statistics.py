import math

def calculateStats(numbers):

  keys = ["avg", "max", "min"]
  vals = []

  if type(numbers) is list:

    if len(numbers) == 0:

      vals = [math.nan for i in keys]
      # print(vals)

    else:

      vals = [ round((sum(numbers) / len(numbers)), 3), max(numbers), min(numbers) ] 
  
  else:

    return

  stats = dict(zip(keys, vals))

  return stats

class EmailAlert:

  def __init__(self):
    self.emailSent = False # by default

class LEDAlert:

  def __init__(self):
    self.ledGlows = False # by default

class StatsAlerter:

  def __init__(self, maxThresh, alertArrs):

    self.maxThresh = maxThresh
    self.alertArrs = alertArrs

  def checkAndAlert(self, numbers):

    stats = calculateStats(numbers)

    if stats["max"] > self.maxThresh:

      self.alertArrs[0].emailSent = True
      self.alertArrs[1].ledGlows = True

# print(calculateStats([]))
# print(calculateStats(["a", "b", "c", "d"])) # type error: unsupported operand types. test case?
# print(calculateStats("a string"))
# print(math.nan)

