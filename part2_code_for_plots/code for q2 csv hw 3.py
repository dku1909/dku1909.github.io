# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 16:26:06 2025

@author: Daniel Ku
"""

import pandas as pd

# Load your dataset (replace 'socialMedia.csv' with your actual file name)
df = pd.read_csv('Downloads/DS 4200/HW 3/socialMedia.csv')

# Group by 'Platform' and 'PostType', then calculate the average 'Likes'
average_likes = df.groupby(['Platform', 'PostType'])['Likes'].mean().reset_index()

average_likes['Likes'] = average_likes['Likes'].round(2)


# Save the result to a new CSV file (replace 'average_likes.csv' with your desired output file name)
average_likes.to_csv('Downloads/DS 4200/HW 3/SocialMediaAvg.csv', index=False)

print(average_likes)