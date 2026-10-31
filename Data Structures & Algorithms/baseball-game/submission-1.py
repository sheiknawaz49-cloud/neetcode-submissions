class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in operations:
            match i:
                case '+':
                    if len(records) >1 :
                        records.append(records[-1]+ records[-2])
                case 'C':
                    records.pop()
                case 'D':
                    records.append(records[-1]*2)
                case _:
                    records.append(int(i))
        return sum(records)
        