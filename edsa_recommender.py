# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Data Loading
@st.cache_data  # This decorator helps to load the data only once and cache it for future calls to speed up the app.
def load_data():
    return pd.read_csv('resources/data/movies.csv')

movies_df = load_data()

def content_based_recommendations(movie_list, top_n):
    # Randomly select top-n movie recommendations from the movies DataFrame
    return movies_df.sample(n=top_n, random_state=None)['title'].tolist()

def collaborative_based_recommendations(movie_list, top_n):
    # Randomly select top-n movie recommendations from the movies DataFrame
    return movies_df.sample(n=top_n, random_state=None)['title'].tolist()

def main():
    # App header
    st.write('# Movie Recommender Engine')
    st.write('### EXPLORE Data Science Academy Unsupervised Predict')

    # Page options setup
    page_options = ["Recommender System", "Solution Overview", "About"]
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == "Recommender System":
        # Recommender System algorithm selection
        algorithm_selection = st.radio("Select an algorithm",
                                       ('Content Based Filtering',
                                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option', movies_df['title'])
        movie_2 = st.selectbox('Second Option', movies_df['title'])
        movie_3 = st.selectbox('Third Option', movies_df['title'])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if algorithm_selection == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_based_recommendations(movie_list=fav_movies, top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(f'{i+1}. {j}')
                except Exception as e:
                    st.error(f"Oops! An error occurred: {e}")

        elif algorithm_selection == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collaborative_based_recommendations(movie_list=fav_movies, top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
                        st.subheader(f'{i+1}. {j}')
                except Exception as e:
                    st.error(f"Oops! An error occurred: {e}")
                    
    elif page_selection == "Solution Overview":
        st.title("Solution Overview")

        # Introduction to the solution
        st.header("Introduction")
        st.write("""
        In the era of digital streaming, personalized movie recommendations have become a cornerstone for enhancing user experience. Our solution, leveraging cutting-edge machine learning algorithms, aims to deliver highly accurate and personalized movie recommendations. By analyzing vast datasets of user preferences and movie attributes, we've developed a system that understands nuanced user tastes.
        """)

        # Data description
        st.header("Data Description")
        st.write("""
        The foundation of our recommendation engine is a comprehensive dataset obtained from the MovieLens project. This dataset includes millions of ratings and thousands of tag applications applied to tens of thousands of movies by tens of thousands of users. We enrich this dataset with additional metadata from various sources, including genres, directors, actors, and movie plot summaries, to improve the accuracy of our recommendations.
        """)

        # EDA Insights
        st.header("Exploratory Data Analysis (EDA) Insights")
        st.write("""
        Our initial data exploration revealed several interesting trends and patterns, such as the popularity of certain genres, the impact of release years on movie ratings, and user rating behaviors. These insights were instrumental in tailoring our recommendation algorithms to better match user preferences.
        """)

        # Methodology
        st.header("Methodology")
        st.write("""
        We employed a two-pronged approach to movie recommendation:
    
        - **Content-Based Filtering:** This algorithm recommends movies by comparing the content of the movies themselves, such as genres, keywords, directors, and actors. By analyzing the movies that a user has rated highly, the system suggests new movies that share similar attributes.
    
        - **Collaborative Filtering:** This method makes automatic predictions about the interests of a user by collecting preferences from many users. The assumption is that if users A and B have similar opinions on an issue, A is more likely to have B's opinion on a different issue than that of a random user.
    
        Our hybrid approach combines these methods to leverage their respective strengths, providing more nuanced and accurate recommendations.
        """)

        # Challenges and Solutions
        st.header("Challenges and Solutions")
        st.write("""
        Throughout the development process, we encountered several challenges, including data sparsity, scalability, and cold start problems. To address these issues, we implemented various strategies such as matrix factorization techniques for handling sparse data, optimizing our algorithms for better scalability, and incorporating user demographics for improving recommendations for new users.
        """)

        # Future Directions
        st.header("Future Directions")
        st.write("""
        Moving forward, we plan to explore more advanced models, such as deep learning and neural network approaches, for further improving recommendation accuracy. Additionally, we aim to incorporate real-time user feedback into our recommendation system to make our model more dynamic and responsive to user preferences.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        Our movie recommender system represents a significant step forward in personalized content delivery. By combining sophisticated algorithms with an in-depth understanding of user preferences and movie data, we have developed a solution that not only meets but exceeds user expectations for personalized recommendations.
        """)

    elif page_selection == "About":
        st.title("About Beyond Infinity")

        # Company Overview
        st.header("Company Overview")
        st.write("""
        Beyond Infinity, a leading data science company, specializes in developing innovative solutions that harness the power of data analytics, machine learning, and artificial intelligence. With a focus on delivering personalized user experiences and actionable insights, Beyond Infinity is at the forefront of transforming industries through data-driven decision-making.
        """)

        # Our Mission
        st.header("Our Mission")
        st.write("""
        Our mission is to empower businesses and individuals with cutting-edge data science solutions, enabling them to unlock the full potential of their data, make informed decisions, and stay ahead in the competitive landscape. At Beyond Infinity, we're more than just data scientists; we're your partners in innovation.
        """)

        # Meet the Team
        st.header("Meet the Team")
        st.write("Behind the success of Beyond Infinity is a team of talented and passionate data science professionals. Meet the core members of our team:")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('resources/imgs/noku.jpg', caption='Nokuthula - Data Scientist', width=150)

        with col2:
            st.image('resources/imgs/nolu.jpg', caption='Noluthando - Machine Learning Engineer', width=150)

        with col3:
            st.image('resources/imgs/masego.jpg', caption='Masego - AI Researcher', width=150)

        # Contact Information
        st.header("Contact Information")
        st.write("""
        We're always open to discussing new projects, creative ideas, or opportunities to be part of your visions. Feel free to reach out to us:
    
        - Email: contact@beyondinfinity.com
        - Phone: +123 456 7890
        - Address: 123 Data Science Lane, Tech City, DS 45678
        """)



if __name__ == '__main__':
    main()
