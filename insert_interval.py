# given a sroted array of intervals, we have add a new interval maintaining it's sorted beahaviour

# intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]

class Solution:
    def insertInterval(self, intervals, new_interval):
        result = []
        for i, interval in enumerate(intervals):
            if new_interval[1] < interval[0]:  # new interval is smaller than the first interval
                return result + [new_interval] + intervals[i:]
            elif new_interval[0] > interval[1]: # we can append the first interval to our result, if this condition ..
                result.append(interval)
            else:   # now let's check for merging of intervals
                new_interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]

        result.append(new_interval)
        return result
    

if __name__=="__main__":
    # intervals = [[1,3],[6,9]]
    # new_interval = [2,5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]

    s = Solution()
    print(s.insertInterval(intervals, new_interval))


            