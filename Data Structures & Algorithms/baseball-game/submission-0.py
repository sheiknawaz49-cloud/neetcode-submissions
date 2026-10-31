class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in operations:
            match i:
                case '+':
                    if len(records) >1 :
                        records.append(records[-1]+ records[-2])
                    print('+', records)
                case 'C':
                    records.pop()
                    print('C', records)

                case 'D':
                    records.append(records[-1]*2)
                    print('D', records)

                case _:
                    records.append(int(i))
        return sum(records)
        