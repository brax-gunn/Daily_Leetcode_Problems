
from heapq import heapify, heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        
        # sort courses based on deadline time
        courses.sort(key = lambda course: course[1])
        
        timeElapsed = 0
        courseDuration = []
        
        for course in courses:
            if timeElapsed + course[0] <= course[1]:
                heappush(courseDuration, -course[0])
                timeElapsed += course[0]
            
            elif len(courseDuration) > 0 and courseDuration[0] < -course[0]:
                timeElapsed += heappop(courseDuration)
                heappush(courseDuration, -course[0])
                timeElapsed += course[0]
            else:
                pass
            
        return len(courseDuration)
        
        
        