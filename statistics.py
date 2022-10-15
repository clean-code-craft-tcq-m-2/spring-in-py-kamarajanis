import math
def calculateStats(numbers):
  if len(numbers)==0:
    return {"avg":math.nan,"max":math.nan,"min":math.nan,}
  return {"avg":sum(numbers)/len(numbers),"max":max(numbers),"min":min(numbers)}


class EmailAlert:
  emailSent=False # By Default email sent is False , Change to True if checkAndAlert function identifies a maxThreshold

class LEDAlert:
  ledGlows=False # By Default led Glows is False , Change to True if checkAndAlert function identifies a maxThreshold


class StatsAlerter:
  def __init__(self,maxThreshold,alertfunction):
    self.maxThershold=maxThreshold
    self.alertfunction=alertfunction

  def checkAndAlert(self,numbers):
    self.numbers=numbers
    if max(self.numbers)>self.maxThershold:
      self.alertfunction[0]=True
      self.alertfunction[1]=True
