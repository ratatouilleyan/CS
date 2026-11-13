observations = [1, 2, 3, 4]
frequencies = [7, 4, 11, 9]

count = 0
i = 0
val = 0
rel_freqs = [0] * len(frequencies)
while i <= (len(frequencies) - 1):
    count += frequencies[i]
    i += 1

for (i, f) in enumerate(frequencies):
     val = f / count
     rel_freqs[i] = val

for (o, r) in zip(observations, rel_freqs):
    print(f'{o} : {r}')