🎬 Movie Recommendation System using Python & GUI (Tkinter)

This project is a simple content-based movie recommendation system built using Python. It recommends movies based on user input using cosine similarity on movie overviews. The project includes a minimal graphical user interface (GUI) made with Tkinter.

---

🔧 Technologies Used

- Python  
- Pandas, NumPy, Scikit-learn  
- Tkinter (for GUI)  
- Jupyter/VS Code (for development)

---

📌 Features

- Load and clean a dataset of movies (`movies.csv`)  
- Combine with credits metadata (`credits.csv`)  
- Process text to generate similarity scores  
- Recommend top 5 similar movies based on description  
- Easy-to-use GUI for entering movie names and getting results instantly

---

🖼️ GUI Preview

Here’s how the GUI looks when it runs:

| User Input | Recommendations |
|------------|------------------|
| ![GUI Input](path/to/your/gui_ss.png) | ![Recommendations](path/to/your/gui_ss_output.png) |

> 💡 *You can replace the above image links with actual screenshot paths after uploading images in your repo or GitHub issue.*

---

📁 Dataset (Not Included Due to Size Limit)

To run this project, you’ll need two datasets:

- `tmdb_5000_movies.csv`  
- `credits.csv` *(⚠️ File size > 25MB, not included in this repo)*

You can download the datasets from:

👉 [Google Drive Download Link](https://yourlink.com) *(replace with your own)*

Once downloaded, place both CSV files in the same folder as `movie.py`.

---

🚀 How to Run

1. Make sure Python is installed  
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn
Run the app:

bash
Copy
Edit
python movie.py
A small window will appear — type a movie name and hit Recommend

🚀 Future Improvements

Add support for fuzzy matching if the title is misspelled

Switch to a Flask-based web UI

Integrate poster and IMDb links in output

Add genre/tag-based filtering

✍️ Author

Prabhakar Rayal
B.Tech CSE | Graphic Era Hill University
📍 Rishikesh, Uttarakhand, India
GitHub Profile (update this with your actual GitHub profile link)
