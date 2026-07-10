"""fence"""


def main():
    """main func"""
    x = list(map(int, input().split(" ")))
    y = int(input())
    ll = ((x[0] + x[1])*2) * x[2]
    price = ll* y
    print(ll)
    print(price)

main()
