class Logger:

    def __init__(self):
        self.print_times = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.print_times:
            self.print_times[message] = timestamp
            return True
        
        if self.print_times[message] + 10 <= timestamp:
            self.print_times[message] = timestamp
            return True
        
        return False
        
"""
- map of message to timestamp
- check if message exists in timestamp
- if it doesn't, then should print message
- else, check timestamp
- if printed timestamp is within last 10 seconds don't print
- else, print and update value
"""

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)