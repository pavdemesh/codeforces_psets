# Get input for n and k in one line (STRINGS!)
n, k = input().split()

# Convert strings to int
num_participants = int(n)
ref_participant = int(k)

# Counter for those who advance to next round
counter_winners = 0

# Check if the condition 1 <= k <= n <= 50 is met
if (ref_participant >= 1) and (ref_participant <= num_participants) and (num_participants <= 50):
    # Get scores in one line and store as list of ints
    scores = list(map(int, input().split()))
    # Check if the number of scores is equal to the number of participants
    # And if the scores are in the range 0 to 100
    if (len(scores) == num_participants) and (scores[0] <= 100) and (scores[-1] >= 0):
        # Iterate through the list
        for i in scores:
            # Compare the score against the reference score
            if (i >= scores[ref_participant - 1]) and (i > 0):
                # If equal or greater, increase counter of winners by 1
                counter_winners += 1
        print(counter_winners)
