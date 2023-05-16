import re
import pandas as pd
import matplotlib.pyplot as plt
from itertools import zip_longest


def extract_perplexities(log_file):
    validation_perplexities = []

    with open(log_file, 'r') as file:
        log_lines = file.readlines()

    for line in log_lines:
        match = re.search(r'ppl:\s+(\d+\.\d+)', line)
        if match:
            perplexity = float(match.group(1))
            validation_perplexities.append(perplexity)

    return validation_perplexities


log_files = ["baseline.log", "pre.log", "post.log", "pre2.log"]
all_perplexities = {}


max_length = 0
for log_file in log_files:
    perplexities = extract_perplexities(log_file)
    all_perplexities[log_file] = perplexities
    max_length = max(max_length, len(perplexities))

for log_file, perplexities in all_perplexities.items():
    if len(perplexities) < max_length:
        perplexities += [None] * (max_length - len(perplexities))


df = pd.DataFrame(all_perplexities)
steps = [500 * (i + 1) for i in range(len(df))]
df.insert(0, "Step", steps)


df.to_csv('perplexity_results.csv', index=False)

# create a line chart based on the df
plt.plot(df['Step'], df['baseline.log'], label='baseline', color='#FF00FF') 
plt.plot(df['Step'], df['post.log'], label='post', color = "#FFFF00")
plt.plot(df['Step'], df['pre.log'], label='pre', color = "#009999")
plt.xlabel('Step')
plt.ylabel('Ppl')
plt.legend()
plt.savefig('perplexity_results.png')
plt.show()



