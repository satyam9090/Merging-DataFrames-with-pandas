# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, axis = 1, join='inner', keys=['bronze', 'silver', 'gold'])

# Print medals
print(medals)
