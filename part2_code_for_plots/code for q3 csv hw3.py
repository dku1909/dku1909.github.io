# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:48:18 2025

@author: Daniel Ku
"""


import pandas as pd

# Load your dataset (replace 'socialMedia.csv' with your actual file name)
df = pd.read_csv('Downloads/DS 4200/HW 3/socialMedia.csv')

# Group by 'Platform' and 'PostType', then calculate the average 'Likes'
average_likes = df.groupby(['Date'])['Likes'].mean().reset_index()


# Save the result to a new CSV file (replace 'average_likes.csv' with your desired output file name)
average_likes.to_csv('Downloads/DS 4200/HW 3/SocialMediaTime.csv', index=False)

print(average_likes)