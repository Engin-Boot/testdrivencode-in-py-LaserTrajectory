import statistics

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
    self.emailAlert = self.alertArrs[0]
    self.ledAlert = self.alertArrs[1]

  def checkAndAlert(self, numbers):

    stats = statistics.calculateStats(numbers)

    if stats["max"] > self.maxThresh:

      self.emailAlert.emailSent = True
      self.ledAlert.ledGlows = True