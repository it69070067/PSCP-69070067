"""3d point distance"""


def main():
    """main func"""
    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))
    d = ((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)**0.5
    print(f"{d:.2f}")

main()
