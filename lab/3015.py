"""fsf"""

def main():
    """main func"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    amt = (z//x)*y + z%x
    print(amt*a)

main()
