sample_array = [12, 11, 13, 5, 6]

for i in range(1, len(sample_array)):

    key = sample_array[i]


    j = i-1

    while j >= 0 and key < sample_array[j]:
        sample_array[j + 1] = sample_array[j]
        j -= 1

    sample_array[j + 1] = key

print(sample_array)
