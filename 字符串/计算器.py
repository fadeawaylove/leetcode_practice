"""
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/calculator-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def calculate(self, s: str) -> int:
        """变成后缀表达式
        优先级：数字>乘除>加减
        """

        def op_func(x, o, y):
            if o == "*":
                ret = x * y
            elif o == "/":
                ret = x / y
            elif o == "+":
                ret = x + y
            elif o == "-":
                ret = x - y
            else:
                raise Exception("operator %s not allowed" % o)
            return int(ret)

        op1 = ("*", "/")
        # op2 = ("+", "-")
        op2 = ("+",)
        ops = (*op1, *op2)

        # 去掉字符串表达式中的空格，提取出表达式的每个元素（数字或者操作符）
        s1 = s.replace(" ", "").replace("-", "+-")
        s = []
        t = ""
        for xx in s1:
            if xx in ops:
                if t:
                    s.append(t)
                    t = ""
                s.append(xx)
            else:
                t += xx
        s.append(t)
        # 存放数字和存放运算符的栈
        num_stack = []
        op_stack = []  # 优先级高的运算符在栈顶

        for op in s:
            # 数字直接进入到数字栈中
            if op not in ops:
                num_stack.append(op)
            # 乘除法需判断是否优先级大于栈顶
            # elif op in op1:
            #     while op_stack:
            #         if op_stack[-1] in op1:
            #             num_stack.append(op_stack.pop())
            #         else:
            #             break
            #     op_stack.append(op)
            # 加减法
            else:
                while op_stack:
                    if op_stack[-1] in op1:
                        num_stack.append(op_stack.pop())
                    else:
                        break
                op_stack.append(op)
        # 进行计算
        stack = num_stack + op_stack[::-1]
        print(stack)
        nums = []
        for op in stack:
            if op not in ops:
                nums.append(int(op))
            else:
                a = nums.pop()
                b = nums.pop()
                nums.append(op_func(b, op, a))
        return int(nums[0])

#
# print(Solution().calculate("1+1-1"))
# print(Solution().calculate(" 3+5 / 2 "))
# print(Solution().calculate("1-1+1"))
# print(Solution().calculate("0-1"))
# print(Solution().calculate("2*3+4"))
print(Solution().calculate("14/3*2"))
