import math

def calculateStats(numbers):

  keys = ["avg", "max", "min"]
  vals = []

  if type(numbers) is list:

    if len(numbers) == 0:

      vals = [math.nan for i in keys] # is_nan test
      # print(vals)

    else:

      vals = [ round((sum(numbers) / len(numbers)), 3), max(numbers), min(numbers) ] # min_max_report test 
  
  else:

    return # invalid_arg test

  stats = dict(zip(keys, vals))

  return stats

# below: alerts tests

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


