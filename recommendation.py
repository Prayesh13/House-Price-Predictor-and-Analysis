import joblib
import pandas as pd

location_df = joblib.load('datasets/location_df.joblib')
desc_df = joblib.load('datasets/desc_df.joblib')

cosine_sim1 = joblib.load('Model/sim1.joblib')
cosine_sim2 = joblib.load('Model/sim2.joblib')

df = pd.read_csv("datasets/re_apartment.csv")


def recommend_properties_by_description(property_name, top_n=10):
    
    cosine_sim_matrix = cosine_sim2
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[desc_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = desc_df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScores': top_scores
    })
    
    return recommendations_df

def recommend_properties_by_distance(property_name, top_n=10):
    cosine_sim_matrix = cosine_sim1

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # sort the properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]

    # Retrives the names of the top properties using indices
    top_properties = location_df.index[top_indices].to_list()

    # create a dataframe with final results
    recommendation_df = pd.DataFrame({
        'PropertyName' : top_properties,
        'SimilarityScores' : top_scores
    })

    return recommendation_df

