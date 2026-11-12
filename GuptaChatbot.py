import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Netflix Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# CUSTOM DESIGN
# -----------------------------

st.markdown("""
<style>
.stApp {
    background-color: #141414;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.movie-card {
    background: #252525;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #444;
}

.stButton button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD AND PROCESS DATA
# -----------------------------

@st.cache_data
def load_data():

    data = pd.read_csv("C:/Users/HP/Downloads/netflix.csv")

    data = data.iloc[:, :5].copy()

    data = data.dropna(
        subset=["Name", "Category"]
    )

    data = data.drop_duplicates(
        subset=["Name"]
    )

    data["Year"] = pd.to_numeric(
        data["Year"], errors="coerce"
    )

    data["Year"] = data["Year"].fillna(
        data["Year"].median()
    ).astype(int)

    data["Age Rating"] = data["Age Rating"].fillna(
        "Not Rated"
    )

    data["Duration"] = data["Duration"].fillna(
        "Unknown"
    )

    data["Name"] = data["Name"].str.lower()
    data["Category"] = data["Category"].str.lower()
    data["Age Rating"] = data["Age Rating"].str.lower()

    data["Combined_Features"] = (
        data["Name"] + " " +
        data["Category"] + " " +
        data["Category"] + " " +
        data["Category"] + " " +
        data["Age Rating"]
    )

    return data.reset_index(drop=True)


df = load_data()

# -----------------------------
# NLP MODEL
# -----------------------------

@st.cache_resource
def create_model(text_data):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform(text_data)

    similarity = cosine_similarity(matrix)

    return similarity


cosine_sim = create_model(
    df["Combined_Features"]
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🎬 Netflix Movie Recommender")

st.write(
    "Discover movies similar to your favourite movies "
    "using Natural Language Processing."
)

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("⚙️ Recommendation Settings")

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=10,
    value=5
)

st.sidebar.write("Powered by NLP + TF-IDF")

# -----------------------------
# MOVIE SELECTION
# -----------------------------

movie_list = sorted(df["Name"].unique())

selected_movie = st.selectbox(
    "🔍 Select your favourite movie",
    movie_list,
    index=None,
    placeholder="Search for a movie..."
)

# -----------------------------
# RECOMMENDATION FUNCTION
# -----------------------------

def recommend_movies(movie_name, top_n):

    movie_index = df[
        df["Name"] == movie_name
    ].index[0]

    scores = list(
        enumerate(cosine_sim[movie_index])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    scores = [
        item for item in scores
        if item[0] != movie_index
    ][:top_n]

    result = []

    for index, score in scores:

        movie = df.iloc[index]

        result.append({
            "Movie": movie["Name"].title(),
            "Year": movie["Year"],
            "Category": movie["Category"].title(),
            "Age Rating": movie["Age Rating"],
            "Duration": movie["Duration"],
            "Similarity": round(score * 100, 2)
        })

    return pd.DataFrame(result)


# -----------------------------
# DISPLAY RECOMMENDATIONS
# -----------------------------

if st.button("✨ Recommend Movies", use_container_width=True):

    if selected_movie:

        recommendations = recommend_movies(
            selected_movie,
            top_n
        )

        st.subheader(
            f"Movies similar to {selected_movie.title()}"
        )

        for i, row in recommendations.iterrows():

            st.markdown(
                f"""
                <div class="movie-card">
                    <h3>🎬 {i+1}. {row['Movie']}</h3>
                    <p>📅 Year: {row['Year']}</p>
                    <p>🎭 Category: {row['Category']}</p>
                    <p>🔞 Age Rating: {row['Age Rating']}</p>
                    <p>⏱️ Duration: {row['Duration']}</p>
                    <p>⭐ Similarity: {row['Similarity']}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.success("Recommendations generated successfully!")

    else:

        st.warning("Please select a movie first.")

# -----------------------------
# DATASET OVERVIEW
# -----------------------------

st.divider()

st.subheader("📊 Netflix Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Movies",
        len(df)
    )

with col2:
    st.metric(
        "Movie Categories",
        df["Category"].nunique()
    )

with col3:
    st.metric(
        "Release Years",
        df["Year"].nunique()
    )

# -----------------------------
# CATEGORY CHART
# -----------------------------

st.subheader("🎭 Top Movie Categories")

category_count = (
    df["Category"]
    .value_counts()
    .head(10)
)

st.bar_chart(category_count)

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "Netflix Movie Recommendation System | "
    "Python | NLP | TF-IDF | Cosine Similarity"
)
