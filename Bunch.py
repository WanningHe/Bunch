
class Bunch:
    def brot(bunch: str):
        '''The Banana Rotator rotates all bananas in a bunch.'''
        result = ""
        for char in bunch:
            if char == '(': 
                result += ')'
            elif char == ')':
                result += '('
            else:
                result += char
        return result
    
    def balign(bunch: str, direction: str = None):
        '''The Banana Aligner aligns all bananas in a bunch.'''
        dir = direction.lower() if direction else None
        result = ""
        count = 0
        
        if dir == 'left' or dir == 'l':
            for char in bunch:
                result += ')' if char == '(' else char
        elif dir == "right" or dir == 'r':
            for char in bunch:
                result += '(' if char == ')' else char

        else:
            for char in bunch:
                if char == '(':
                    dir = 'right'
                    count += 1
                    break
                elif char == ')':
                    dir = 'left'
                    count += 1
                    break
            if count <= 0:
                return bunch
            else:
                result = Bunch.balign(bunch, direction=dir)
        return result