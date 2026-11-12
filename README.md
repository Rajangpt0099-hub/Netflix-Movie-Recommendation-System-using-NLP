# 🎬 Netflix Movie Recommendation System using NLP

## 📌 Project Overview

The **Netflix Movie Recommendation System using Natural Language Processing (NLP)** is a content-based recommendation system that suggests similar movies based on movie titles, categories, and age ratings.

The project uses **TF-IDF Vectorization** and **Cosine Similarity** to identify similarities between movies and generate relevant recommendations.

An interactive Streamlit application allows users to search for their favourite movies and discover similar movies easily.

## 🎯 Project Objectives

- Build a movie recommendation system using NLP techniques.
- Perform data cleaning and exploratory data analysis (EDA).
- Apply TF-IDF Vectorization to convert text into numerical features.
- Calculate movie similarities using Cosine Similarity.
- Recommend movies based on user search input.
- Develop an interactive and user-friendly Streamlit application.

## 📂 Dataset Information

The project uses a Netflix movie dataset (`netflix.csv`).

**Important features:**

- Name – Movie title.
- Year – Movie release year.
- Age Rating – Movie age classification.
- Duration – Movie duration.
- Category – Movie genre or category.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| NLP | Text processing |
| TF-IDF | Text vectorization |
| Cosine Similarity | Movie similarity calculation |
| Streamlit | Interactive web application |

## ⚙️ Project Workflow

**1. Data Collection**
- Load the Netflix dataset using Pandas.
- Understand the dataset structure and features.

**2. Data Cleaning**
- Handle missing values.
- Remove duplicate movie records.
- Clean and prepare text columns.

**3. Exploratory Data Analysis (EDA)**
- Analyze movie categories.
- Explore release-year distribution.
- Analyze age ratings.
- Identify popular movie categories.

**4. Natural Language Processing (NLP)**
- Combine movie titles, categories, and age ratings.
- Perform text preprocessing.
- Convert text into numerical vectors using TF-IDF.

**5. Recommendation Model**
- Calculate similarity scores using Cosine Similarity.
- Identify movies with similar features.
- Generate Top-N movie recommendations.

**6. Streamlit Application**
- Search movies using a text input.
- Find matching movie titles.
- Display similar movie recommendations.
- Show movie information and similarity scores.
- Explore interactive dataset visualizations.

## 🧠 Recommendation Algorithm

This project uses a Content-Based Filtering approach.

**TF-IDF Vectorization:**

Converts movie-related text into numerical representations based on the importance of words.

**Cosine Similarity:**

Measures the similarity between movie feature vectors.

The movies with the highest similarity scores are selected as recommendations.

## 📊 Key Project Insights

- Comedies and thriller movies are among the most represented categories.
- Kids & Family Movies and Romantic Movies also have significant representation.
- The dataset contains movies released across multiple years.
- NLP techniques help identify similar movies based on available metadata.

## 🚀 Installation and Setup

**Step 1: Clone the Repository**

```bash
git clone https://github.com/Rajangpt0099-hub/Netflix-Movie-Recommendation-System-using-NLP.git
```

**Step 2: Navigate to the Project Folder**

```bash
cd Netflix-Movie-Recommendation-System-using-NLP
```

**Step 3: Install Required Libraries**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

**Step 4: Run the Streamlit Application**

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
Netflix-Movie-Recommendation-System-using-NLP/
│
├── netflix.csv
├── app.py
├── README.md
│
└── requirements.txt
```

## 💡 Future Enhancements

- Integrate movie posters and images.
- Add movie descriptions and plot-based recommendations.
- Implement advanced NLP techniques.
- Add genre-based filtering.
- Improve recommendation relevance.
- Deploy the application using Streamlit Cloud.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data Cleaning and Data Preprocessing.
- Exploratory Data Analysis.
- Natural Language Processing.
- TF-IDF Vectorization.
- Cosine Similarity.
- Content-Based Recommendation Systems.
- Python and Scikit-learn.
- Interactive Dashboard Development using Streamlit.
<img width="1887" height="1021" alt="image" src="https://github.com/user-attachments/assets/e6a31cf4-7b10-403c-9713-09c8cfe732b7" />
<img width="1903" height="1008" alt="image" src="https://github.com/user-attachments/assets/3a5ab1fe-ccfe-42d0-bff8-61c25fb5ae9b" />
<img width="1892" height="1030" alt="image" src="https://github.com/user-attachments/assets/2a3e5b25-4fb8-418b-a826-420b91de2f6d" />
<img width="1902" height="956" alt="image" src="https://github.com/user-attachments/assets/441af8b3-1e6e-4d29-ad8a-85372eceadf6" />
<img width="1433" height="862" alt="image" src="https://github.com/user-attachments/assets/c65a6250-05bb-4911-a6d2-5852bebe0c82" />

## 👨‍💻 Author

**Rajan Gupta**

GitHub: [Rajangpt0099-hub](https://github.com/Rajangpt0099-hub)

LinkedIn: [Connect with me](https://www.linkedin.com/in/rajangupta0099/)

---

⭐ If you find this project interesting, don't forget to star the repository!

**#Python #NLP #MachineLearning #RecommendationSystem #TFIDF #CosineSimilarity #Streamlit #DataScience #Netflix**
