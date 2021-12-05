from day04a import numbers, boards

def main():
    last_score = 0
    for n in numbers:
        for b in boards:
            # skip if the Bingo board already won
            if b.skip:
                continue
            b.draw(n)
            if b.winner():
                last_score = n * b.unmarked_sum()
                print(last_score)
    return last_score

if __name__ == '__main__':
    print(main())