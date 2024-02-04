import logging
import gensim


class W2V:
    def __init__(self, w2v_flat_file_path):
        """
        Represents loaded W2V model.

        Args:
            w2v_flat_file_path (str): Path to Word2Vec CSV file.
        """
        self.logger = logging.getLogger(__name__)
        self.w2v_flat_file_path = w2v_flat_file_path
        self.model = self.load_embeddings()

    def load_embeddings(self):
        """
        Load Word2Vec embeddings from CSV file.

        Returns:
            gensim.models.KeyedVectors: Word2Vec model.
        """
        try:
            model = gensim.models.KeyedVectors.load_word2vec_format(self.w2v_flat_file_path)
            self.logger.info("W2V data loaded successfully.")
            return model
        except Exception as e:
            self.logger.error(f"Failed to load W2V data: {e}")
            raise

    def get_word_vector(self, word):
        """
        Get vector representation of a word from model.

        Args:
            word (str): Word to retrieve the vector for.

        Returns:
            np.ndarray: Vector representation of the word.
        """
        try:
            return self.model[word]
        except KeyError:
            self.logger.warning(f"Attention! Word '{word}' not in provided vocabulary(model).")
            return None

