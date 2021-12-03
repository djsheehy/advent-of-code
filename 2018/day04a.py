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

# Get laziest guard (longest sleep time).
nap_length = {}
for g, intervals in naps.items():
    for n in intervals:
        if g in nap_length:
            nap_length[g] += (n[1] - n[0])
        else:
            nap_length[g] = n[1] - n[0]

laziest = max(nap_length.items(), key=lambda x: x[1].seconds)[0]
print("Laziest guard:", laziest)

# Get most-slept minute.
minutes = [0] * 60
for (start, stop) in naps[laziest]:
    date = start
    while date <= stop:
        minutes[date.minute] += 1
        date += minute

bestmin = max(enumerate(minutes), key=lambda x: x[1])[0]
print("Laziest minute:", bestmin)
print("Answer:", laziest * bestmin)