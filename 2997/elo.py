"""sfsas"""


def main():
    """hell na"""
    RA = int(input())
    RB = int(input())
    A_B = input()
    if A_B == "A":
        EA = 1/ (1 + 10 **((RB-RA)/400))
        print(f"{EA:.2f}")
    elif A_B == "B":
        EB = 1/ (1 + 10 **((RA-RB)/400))
        print(f"{EB:.2f}")

main()
