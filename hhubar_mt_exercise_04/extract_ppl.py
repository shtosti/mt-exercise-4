import re

log_file = "/Users/shtosti/Dropbox/study/UZH/SS23/Machine_Translation/exercises/mt_2023_exercise_4/mt-exercise-4/logs/deen_transformer_pre/err"
validation_perplexities = []

# Open the log file
with open(log_file, 'r') as file:
    log_lines = file.readlines()

# Search for perplexity values and extract them
for line in log_lines:
    # Use regular expressions to find lines containing perplexity values
    match = re.search(r'ppl:\s+(\d+\.\d+)', line)
    if match:
        perplexity = float(match.group(1))
        validation_perplexities.append(perplexity)

# Print the extracted validation perplexities
for perplexity in validation_perplexities:
    print(perplexity)

with open('pre_perplexities.txt', 'w') as file:
    for perplexity in validation_perplexities:
        file.write(str(perplexity) + '\n')



