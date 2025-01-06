class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        calendar = self.calendar
        if not calendar: 
            calendar.append((start, end))
        else:
            for (pre_start, pre_end) in calendar:
                if not(pre_end <= start or pre_start >= end):
                    return False
            calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)