import pandas as pd

df = pd.read_csv("normal_info.csv", ',',  index_col=0)
df = df.loc[df['filename'] == "mm/memory.c"]

df.to_csv("memory.csv")
sum_of_additions = df['n_additions'].sum()
sum_of_deletions = df['n_deletions'].sum()

df['total_additions'] = sum_of_additions
df['total_deletions'] = sum_of_deletions

authors = df['author_id'].unique()

# Add empty column that will be filled with the author information
df['author_total_additions'] = 0
df['author_total_deletions'] = 0

for author in authors:
	df_author = df.loc[df['author_id'] == author, ]
	sum_of_author_additions = df_author['n_additions'].sum()
	sum_of_author_deletions = df_author['n_deletions'].sum()
	df.loc[df['author_id'] == author, 'author_total_additions'] = sum_of_author_additions
	df.loc[df['author_id'] == author, 'author_total_deletions'] = sum_of_author_deletions

df.to_csv("memory.csv")
print(authors)