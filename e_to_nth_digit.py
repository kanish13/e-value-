import math

def cal_e_value(num):
    value=round(math.e,num)
    return value

if __name__=="__main__":
    num=int(input("Enter the number till which you want the e value:"))
    print(cal_e_value(num))
