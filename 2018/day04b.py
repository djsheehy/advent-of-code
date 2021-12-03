from datetime import datetime, timedelta

f = open('input04.txt')
data = f.readlines()
f.close()

def convert(line):
    "Extract datetime and message from a line."
    date, msg = line.split('] ')
    date = date[1:]
    date = datetime.strptime(date, "%Y-%m-%d %H:%M")
    return (date, msg.strip())

def guardnum(msg):
    "Extract guard number from a message."
    n = msg.split()[1][1:]
    return int(n)

data = [convert(x) for x in data]
data.sort()

# collect sleeping intervals for each guard.
naps = {}
sleep_start = None
sleep_stop = None
guard = 0
minute = timedelta(seconds=60)

for date, msg in data:
    if msg == 'falls asleep':
        sleep_start = date
    elif msg == 'wakes up':
        sleep_stop = date - minute
        if guard in naps:
            naps[guard].append([sleep_start, sleep_stop])
        else:
            naps[guard] = [[sleep_start, sleep_stop]]
    else:
        guard = guardnum(msg)

# Which guard is most frequently asleep on the same minute?
histogram = {}
for g in naps:
    histogram[g] = [0] * 60
    for start, stop in naps[g]:
        time = start
        while time <= stop:
            histogram[g][time.minute] += 1
            time += minute

max_histogram = {}
for g in histogram:
    max_histogram[g] = max(enumerate(histogram[g]), key=lambda x: x[1])

best_guard, best_minute = max(max_histogram.items(), key=lambda x: x[1][1])
print(best_guard * best_minute[0])