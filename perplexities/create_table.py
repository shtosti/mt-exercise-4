# import re
# import pandas as pd


# def extract_perplexities(log_file):
#     validation_perplexities = []

#     with open(log_file, 'r') as file:
#         log_lines = file.readlines()

#     for line in log_lines:
#         match = re.search(r'ppl:\s+(\d+\.\d+)', line)
#         if match:
#             perplexity = float(match.group(1))
#             validation_perplexities.append(perplexity)

#     return validation_perplexities


# log_files = ["baseline.log", "pre.log"]
# all_perplexities = []

# for log_file in log_files:
#     perplexities = extract_perplexities(log_file)
#     all_perplexities[log_file] = perplexities


# df = pd.DataFrame(all_perplexities)
# # steps = [500 * (i + 1) for i in range(len(df))]
# # df.index = steps


# df.to_csv('perplexity_results.csv', index=False)


import re
import pandas as pd


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


log_files = ["baseline.log", "pre.log"]
all_perplexities = {}

for log_file in log_files:
    perplexities = extract_perplexities(log_file)
    all_perplexities[log_file] = perplexities


df = pd.DataFrame(all_perplexities)
steps = [500 * (i + 1) for i in range(len(df))]
df.insert(0, "Step", steps)


df.to_csv('perplexity_results.csv', index=False)
