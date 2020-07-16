*******************************************************************
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
examples:

Input: hour = 12, minutes = 30
Output: 165

Input: hour = 3, minutes = 30
Output: 75
*******************************************************************
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h=(hour%12 + minutes/60)*30
        m=minutes*6
        angle=fabs(h-m)
        if angle>180:
            angle=360-angle
        return angle
        
