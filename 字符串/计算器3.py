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
import re


# 不使用栈的方法 使用正则 先计算全部的乘除 在计算加减法
class Solution:
    def calculate(self, s: str) -> int:
        """
        先计算乘除 再计算加减
        :param s:
        :return:
        """
        # 去除空格
        s = re.sub(r"([+*/])", r" \g<1> ", s.replace(" ", "").replace(r"-", "+-")).split()  # 正则标记出操作符
        print(s)

        # 将运算符和数字分开存两个列表
        ret = [int(s[0])]
        for num_and_opera in zip(s[2::2], s[1::2]):
            num, opera = num_and_opera
            if opera == "*":
                ret[-1] *= int(num)
            elif opera == "/":
                if ret[-1] < 0:
                    ret[-1] = -((-ret[-1]) // int(num))
                else:
                    ret[-1] //= int(num)
            else:
                ret.append(int(num))
        # print(ret)
        return sum(ret)


# print(Solution().calculate("1+1-1"))
# print(Solution().calculate(" 3+5 / 2 "))
# print(Solution().calculate("1-1+1"))
# print(Solution().calculate("0-1"))
# print(Solution().calculate("2*3+4"))
# print(Solution().calculate("14/3*2"))
# print(Solution().calculate("14-3/2"))
print(Solution().calculate("10000-1000/10+100*1"))
