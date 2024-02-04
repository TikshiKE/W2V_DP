import pandas as pd
import numpy as np
from scipy.spatial import distance


class SimilarityCalc:
    def __init__(self, w2v_model):
        """
        Represent the operations for similarity identifications.

        Args:
            w2v_model: A Word2Vec model.
        """
        self.w2v_model = w2v_model

    def phrase_to_vec(self, phrase):
        """
        Clear, tokenize and convert words to vectors, then calculate the mean

        Args:
            phrase (str): Input phrase.

        Returns:
            np.ndarray: Vector representation of input phrase.
        """
        phrase.strip().strip('"').strip('?').split()
        words = phrase.split()
        vectors = [self.w2v_model.get_word_vector(word) for word in words if
                   self.w2v_model.get_word_vector(word) is not None]
        if vectors:
            return np.mean(vectors, axis=0)
        return None

    @staticmethod
    def calculate_distance(vec1, vec2, metric='euclidean'):
        """
        Calculate distance between two vectors (default by Euclidean method)

        Args:
            vec1 (np.ndarray): First vector.
            vec2 (np.ndarray): Second vector.
            metric (str): Calculation method to use ('euclidean' or 'cosine').

        Returns:
            float: Distance between two vectors.
        """
        if vec1 is None or vec2 is None:
            return float('inf')  # Return a infinite positive value to represent "infinite" distance
        vec1 = np.array(vec1).flatten()
        vec2 = np.array(vec2).flatten()
        if metric == 'cosine':
            return distance.cosine(vec1, vec2)
        else:  # default to Euclidean if anything else is provided
            return distance.euclidean(vec1, vec2)

    def batch_process(self, phrases_path, output_path):
        """
        Process phrases from csv file and save results to output file.

        Args:
            phrases_path (str): Path to input CSV file with phrases.
            output_path (str): Path for output CSV file.
        """
        phrases_df = pd.read_csv(phrases_path, skiprows=1, header=None, names=['phrase'], encoding='ISO-8859-1')
        phrases_df['vector'] = phrases_df['phrase'].apply(lambda x: self.phrase_to_vec(x))
        results = []

        for i, row in phrases_df.iterrows():
            curr_vector = row['vector']
            distances = []
            for j, comp_row in phrases_df.iterrows():
                comp_vector = comp_row['vector']
                if comp_vector is not None and curr_vector is not None:
                    dist = self.calculate_distance(curr_vector, comp_vector)
                    distances.append(dist)
                else:
                    distances.append(float('inf'))
            results.append(distances)

        # Save the results to the output file
        distance_df = pd.DataFrame(results, index=phrases_df['phrase'], columns=phrases_df['phrase'])
        distance_df.to_csv(output_path)

    def find_closest_phrase(self, user_input, phrases_df):
        """
        Find the closest phrase to user input by W2V vectors distance.

        Args:
            user_input (str): User input phrase.
            phrases_df (pd.DataFrame): DataFrame containing phrases from phrase.csv.

        Returns:
            str: Closest phrase.
            float: Calculated distance to closest phrase.
        """
        user_vec = self.phrase_to_vec(user_input)
        min_distance = float('inf')
        closest_phrase = None
        for i, row in phrases_df.iterrows():
            phrase_vec = self.phrase_to_vec(row['phrase'])
            if phrase_vec is not None:
                dist = self.calculate_distance(user_vec, phrase_vec)
                if dist < min_distance:
                    min_distance = dist
                    closest_phrase = row['phrase']
        return closest_phrase, min_distance
