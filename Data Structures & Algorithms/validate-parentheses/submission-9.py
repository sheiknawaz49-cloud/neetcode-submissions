class Solution:
    def isValid(self, s: str) -> bool:
        dict_b = {
            '(' : ')',
            '[': ']',
            '{': '}'
        }
        n = len(s)
        l =[]
        if n%2 ==0:
            for i in range(n):
                if s[i] in dict_b:
                    print('insideif')
                    l.append(s[i])
                else:
                    if len(l) and dict_b.get(l[-1]) ==s[i] :
                        l.pop()
                    else:
                        print('else',l,s[i])
                        return False
            return True if len(l)==0 else False
            
        return False
        