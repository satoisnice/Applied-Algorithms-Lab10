def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1): # gives us length of wat to search, decrement length by 1 each time as the largest item will end up at the end GUARANTEED
        for i in range(0, j):            # sweeps thru the sequence, length determined by loop above it
            if seq[i] > seq[i+1]:        # comparison check
                seq[i], seq[i+1] = seq[i+1], seq[i] # swap pair if true

def selection_sort(seq):
    start_line = 0
    for j in range(len(seq)): 
        low_index = j 
        for i in range(j, len(seq)):                  
            if seq[low_index] > seq[i]:
                low_index = i
        seq[j], seq[low_index] = seq[low_index], seq[j]
        # start_line += 1

def insertion_sort(seq):
    start_line = 0
    for _ in range(len(seq)):
        low_index