class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_stack = []
        my_list = []
        for i in range(len(position)):
            my_list.append((position[i], speed[i]))
        my_list.sort(key=lambda x: x[0])

        for i in my_list:
            time = (target - i[0])/i[1]
            while my_stack and my_stack[-1] <= time:
                my_stack.pop()
            my_stack.append(time)

        return len(my_stack)