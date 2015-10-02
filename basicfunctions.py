def main():
    levelnum = 0
    score = 0
    while levelnum < 9:
        level(levelnum)
        print levelnum
        levelnum += 1
def level(num1):
    time = 3 - (num1 * 0.25)
    count = 0
    while count < 10:
        randomcard()
        count += 1
main()

