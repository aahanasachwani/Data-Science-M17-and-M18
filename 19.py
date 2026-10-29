# Recommendation Engine — Part 2

### Step 1 — Enter Your Ratings

user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5},
]

movies_input = pd.DataFrame(user_input)
movies_input


### Step 2 — Merge With Movie IDs

input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]
movies_input = pd.merge(input_id, movies_input)
movies_input = movies_input.drop(['genres', 'year'], axis=1)
movies_input


### Step 3 — Build Taste Profile

movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]
movies_user = movies_user.reset_index(drop=True)

UserGenreTable = movies_user.drop(['movieId', 'title', 'genres', 'year'], axis=1)

UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])
UserProfile


### Step 4 — Plot Taste Profile

plt.figure(figsize=(10, 5))
plt.bar(UserProfile.index, UserProfile.values, color='#FF6B6B')
plt.title('Your Taste Profile')
plt.xlabel('Genre')
plt.ylabel('Weight')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


### Step 5 — Score All Movies

GenreTable = movies_copy.set_index(movies_copy['movieId'])
GenreTable = GenreTable.drop(['movieId', 'title', 'genres', 'year'], axis=1)

Recommendation_df = ((GenreTable * UserProfile).sum(axis=1)) / UserProfile.sum()
Recommendation_df = Recommendation_df.sort_values(ascending=False)
Recommendation_df.head()


### Step 6 — Get Top Recommendations

RecommendationTable = movies_df.loc[movies_df['movieId'].isin(Recommendation_df.head(20).keys())]
RecommendationTable


### Step 7 — Plot Top Picks

top10_scores = Recommendation_df.head(10)
top10_titles = movies_df.set_index('movieId').loc[top10_scores.index]['title']

plt.figure(figsize=(8, 6))
plt.barh(top10_titles[::-1], top10_scores.values[::-1], color='#51CF66')
plt.title('Top 10 Picks')
plt.xlabel('Match Score')
plt.tight_layout()
plt.show()
