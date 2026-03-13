import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Using the csv file you provided in the data folder
df = pd.read_csv("data/spotify_songs.csv")

# Quick check to see if the data loaded correctly
print("First few rows of our Spotify data:")
print(df.head())

# Checking for any empty cells so they don't break the model later
print("\nChecking for missing values...")
print(df.isnull().sum())

# Dropping the few rows that have missing values (mostly track names/artists)
df = df.dropna()
print(f"Cleaned dataset shape: {df.shape}")

# Let's see how many songs we have for each genre
plt.figure(figsize=(10,5))
sns.countplot(x='playlist_genre', data=df)
plt.title("How many songs are in each genre?")
plt.xticks(rotation=45)
plt.show()

# CORRELATION MATRIX: This helps us see which features (like energy and loudness) move together
plt.figure(figsize=(12,8))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation between Audio Features")
plt.show()

# We only want the numerical 'audio features' for clustering
features = ['danceability', 'energy', 'loudness', 'speechiness', 
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
X = df[features]

# SCALING: Since tempo is ~120 and danceability is ~0.7, we scale them 
# so the AI treats them with equal importance.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# I'm choosing 6 clusters to see how the genres group together
kmeans = KMeans(n_clusters=6, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

print("\nAI model training complete! Clusters assigned to each song.")

# Plotting clusters based on Danceability vs Energy to see the 'groups'
plt.figure(figsize=(10,6))
sns.scatterplot(x='danceability', y='energy', hue='cluster', data=df, palette='viridis', alpha=0.5)
plt.title('AI Generated Clusters (Danceability vs Energy)')
plt.show()

# Checking which genres ended up in which clusters
plt.figure(figsize=(12,6))
sns.countplot(x='cluster', hue='playlist_genre', data=df)
plt.title('Which Genres are in which AI Cluster?')
plt.show()

# Saving the final result so we can use it for recommendations later
df.to_csv("spotify_clustered_results.csv", index=False)
print("\nDone! Your final file 'spotify_clustered_results.csv' is ready for submission.")