# Spotify Songs: Genre Segmentation & Clustering
**Project Submission for AI/ML Course** **Student Name:** Lakshay Yadav  
**Submission Date:** March 16, 2026

---

## 📌 Project Overview
The music recommendation system of Spotify is world-class because it understands the "DNA" of a song. This project uses **Unsupervised Machine Learning (K-Means Clustering)** to group 32,000+ songs into clusters based on their auditory features like danceability, energy, and tempo.

The goal is to build an automated system that can categorize music beyond simple genre labels, identifying similar acoustic properties across different styles.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.14
* **Data Handling:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Seaborn`
* **Machine Learning:** `Scikit-Learn` (StandardScaler, KMeans)

---

## 📊 Exploratory Data Analysis (EDA)
Before building the AI model, I performed deep data analysis to extract meaningful insights:

### 1. Genre Distribution
I analyzed how many songs belong to each genre. **EDM** and **Rap** dominate this specific dataset, while **Rock** has the lowest representation.
![Genre Distribution](plots/graph1.png)

### 2. Feature Correlation Matrix
This heatmap shows how musical properties relate to each other. 
* **Key Insight:** Energy and Loudness have a strong positive correlation (**0.68**). 
* **Key Insight:** Acousticness and Energy have a negative correlation, confirming that "plugged-in" songs are generally higher in energy.
![Correlation Heatmap](plots/graph2.png)

---

## 🤖 AI Model: K-Means Clustering
I implemented a Clustering algorithm to group songs into **6 distinct clusters**.

1. **Pre-processing:** Handled missing values using `dropna()`.
2. **Feature Selection:** Focused on 9 numerical attributes (Danceability, Energy, Loudness, etc.).
3. **Scaling:** Used `StandardScaler` to normalize the data so that features with large ranges (like Tempo) don't bias the model.
4. **Clustering:** Trained the KMeans model to find the "center" of each song group.

### Cluster Results
This scatter plot visualizes how the AI separated songs based on their Energy and Danceability levels:
![Song Clusters](plots/graph3.png)

### Genre vs Cluster Mapping
This plot shows how "official" genres are distributed across the "AI-generated" clusters, revealing which genres are sonically similar.
![Genre Clusters](plots/graph4.png)

---

## Final Results & Conclusion
The project successfully generated a new dataset: `spotify_clustered_results.csv`. 

By assigning a `cluster_id` to every song, we have built the logic for a **Recommendation System**. If a user listens to a song in **Cluster 3**, the system can now instantly recommend thousands of other songs that share the exact same acoustic "fingerprint."

---

## 📁 Project Structure
```text
SPOTIFYP1/
├── data/
│   └── spotify_songs.csv            # Input Dataset
├── plots/                           # Generated Visualizations
│   ├── genre_distribution.png
│   ├── correlation_heatmap.png
│   ├── cluster_scatter.png
│   └── genre_vs_cluster.png
├── spotify_project.py               # Main Python Logic
├── spotify_clustered_results.csv    # Final Output with Cluster IDs
└── README.md                        # Project Documentation
