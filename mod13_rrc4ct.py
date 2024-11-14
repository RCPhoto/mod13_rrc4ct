# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:41:39 2024

@author: Robby
"""

import unittest
from datetime import datetime

#validate the stock symbol
def validateSymbol(symbol):
    if not isinstance(symbol, str):
        return False
    if not 1 <= len(symbol) <= 7:
        return False
    if not symbol.isalpha():
        return False
    if not symbol.isupper():
        return False
    return True

#validate the chart type
def validateChartType(chartType):
    if not isinstance(chartType, str):
        return False
    if not (chartType == "1" or chartType == "2"):
        return False
    return True

#validate the time series
def validateTimeSeries(timeSeries):
    if not isinstance(timeSeries, str):
        return False
    if not (timeSeries == "1" or timeSeries == "2" or timeSeries == "3" or timeSeries == "4"):
        return False
    return True
    
#validate the Dates
def validateDate(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
#Test Input class
class TestInputValidation(unittest.TestCase):
    
#validate symbol
   def testValidateSymbol(self):
      self.assertTrue(validateSymbol("AAPL"))
      self.assertTrue(validateSymbol("GOOG"))
      self.assertFalse(validateSymbol("aapl"))
      self.assertFalse(validateSymbol("1234"))
      self.assertFalse(validateSymbol("AAPL1234"))
      self.assertFalse(validateSymbol(""))

#validate chart type
   def testValidateChartType(self):
      self.assertTrue(validateChartType("1"))
      self.assertTrue(validateChartType("2"))
      self.assertFalse(validateChartType("3"))
      self.assertFalse(validateChartType("a"))

#validate time series
   def testValidateTimeSeries(self):
      self.assertTrue(validateTimeSeries("1"))
      self.assertTrue(validateTimeSeries("2"))
      self.assertTrue(validateTimeSeries("3"))
      self.assertTrue(validateTimeSeries("4"))
      self.assertFalse(validateTimeSeries("5"))
      self.assertFalse(validateTimeSeries("a"))

#Validate start and end dates.
   def testValidateDate(self):
      self.assertTrue(validateDate("2023-11-15"))
      self.assertFalse(validateDate("11-15-2023"))
      self.assertFalse(validateDate("2023/11/15"))

if __name__ == '__main__':
    unittest.main()