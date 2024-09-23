# Importing Pandas & numpy
import pandas as pd
import numpy as np

# Importing CSV
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Country Count DF
count_country = df.country.value_counts()

# Obtaining average/mean for each 'country' within column
average_df = df.groupby('country')['points'].mean()

# Rounding points to 1 decimal
average_df = average_df.round(1)

# Combine DFs with "count" & "points" as columns
wine_review = pd.DataFrame({
        'count': count_country,
        'points': average_df
}).reset_index()

# Sorts DF by "count" from highest to lowest
wine_review = wine_review.sort_values(by='count', ascending=False)

# Save DF "wine-review"
wine_review.to_csv('wine_review', index=False)

# Print DF
print(wine_review)
