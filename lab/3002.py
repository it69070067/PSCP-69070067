"""wdwd"""

def main():
    """"main func"""
    name = str(input())
    last_n = str(input())
    age = str(input())
    if len(name) >= 5 and len(last_n) >= 5:
        print(f"{name[0:2]}{last_n[-1]}{age[-1]}")
    else:
        print(f"{name[0]}{age}{last_n[-1]}")

main()
