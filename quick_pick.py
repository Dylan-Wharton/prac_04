import random
def main():
    num_picks = int(input("How many quick picks?"))
    for i in range(num_picks):
        pick_numbers = []
        for i in range(6):
            pick_numbers.append(random.randint(0,45))
        print(" ".join("{:2}".format(number) for number in pick_numbers))

main()
