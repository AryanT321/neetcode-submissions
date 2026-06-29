class Solution:
    def isValid(self, s: str) -> bool:
        conroy = []
        for i in s:
            if i == "(" or i =="{" or i == "[":
                conroy.append(i)
            elif i == "}" and conroy:
                if conroy[-1] == "{":
                    conroy.pop()
                else:
                    return False
            elif i == ")" and conroy:
                if conroy[-1] == "(":
                    conroy.pop()
                else:
                    return False
            elif i =="]" and conroy:
                if conroy[-1] == "[":
                    conroy.pop()
                else:
                    return False
            else:
                return False

        if conroy:
            return False
        return True
            


            
            
            
            