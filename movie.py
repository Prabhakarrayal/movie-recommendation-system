import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk

# Load the credits and movies data from CSV files
credits = pd.read_csv(r"D:\movie rec updated\credits.csv")
movies = pd.read_csv(r"D:\movie rec updated\movies.csv")

# Combine the two datasets on the movie title
movies = movies.merge(credits, on='title')

# Just keep the columns we really need
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# This function takes that weird string and turns it into a list of names
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

# We only want the director's name from the crew list
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

# Just clean up spaces in names to keep things consistent
def collapse(L):
    return [i.replace(" ", "") for i in L]

# Drop any movies that have missing info
movies.dropna(inplace=True)

# Apply the convert function to get genres, keywords, and cast as lists
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
# For cast, we only keep the top 3 actors
movies['cast'] = movies['cast'].apply(convert).apply(lambda x: x[0:3])
# Get the director's name from the crew info
movies['crew'] = movies['crew'].apply(fetch_director)

# Clean spaces from all our lists for uniformity
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
# Split overview into words for better tagging
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Combine all relevant info into one big list of tags for each movie
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Create a new dataframe with just the essential columns
new = movies[['movie_id', 'title', 'tags']]
# Turn the list of tags back into a single string
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

# Convert text data into numbers using CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()

# Calculate similarity between movies based on those vectors
similarity = cosine_similarity(vector)

# This function recommends 5 movies similar to the one you give it
def recommend(movie):
    try:
        # Find the movie index (ignoring case)
        index = new[new['title'].str.lower() == movie.lower()].index[0]
    except IndexError:
        # If movie isn’t found, return an empty list
        return []

    # Get similarity scores with all movies, sorted from most similar
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # Return the top 5 movie titles except the one you searched for
    return [new.iloc[i[0]].title for i in distances[1:6]]

# When you click recommend, this runs
def recommend_movies():
    user_input = entry.get()
    recommended_movies = recommend(user_input)

    if recommended_movies:
        output_label.config(text="Top 5 Recommended Movies:\n" + "\n".join(recommended_movies))
    else:
        output_label.config(text="❌ Movie not found. Please try another title.")

# Close the GUI window properly when clicking Close
def close_tkinter_window():
    window.quit()
    window.destroy()

# Set up the main window
window = tk.Tk()
window.title('🎬 Movie Recommendation System')
window.geometry("400x300")

frame = ttk.Frame(window, padding=10)
frame.pack()

# Label asking for movie input
ttk.Label(frame, text="Enter Movie Title:", font=("Arial", 12)).pack(pady=5)
# Text entry box
entry = ttk.Entry(frame, width=40)
entry.pack(pady=5)

# Button to get recommendations
ttk.Button(frame, text="Recommend", command=recommend_movies).pack(pady=10)

# Where results or errors show up
output_label = ttk.Label(frame, text="", wraplength=350, font=("Arial", 10))
output_label.pack()

# Close button
ttk.Button(frame, text="Close", command=close_tkinter_window).pack(pady=5)

# Start the GUI loop
window.mainloop()



