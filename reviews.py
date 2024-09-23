# Importing Pandas & numpy
import pandas as pd
import numpy as np

# Importing CSV
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Country Count
count_country = df.value_counts('country')

# Obtaining average/mean for each 'country' within column
average_df = df.groupby('country').agg({'points': ['count', 'mean']})

# Rounding points to 1 decimal
average_df = average_df.round(1)

# Remove Multi-Index by resetting the columns
average_df.columns = ['count', 'points']

# Resetting the index to add 'country' back as a column
average_df = average_df.reset_index()

# Sort the DataFrame by 'count' in descending order
average_df = average_df.sort_values(by='count', ascending=False)

# Remove the index column (the old index is not shown if you display the DataFrame)
average_df = average_df.reset_index(drop=True)

# Display the final sorted DataFrame
print(average_df)

#Save file to csv
average_df.to_csv('wine_reviews.csv',index=False)



