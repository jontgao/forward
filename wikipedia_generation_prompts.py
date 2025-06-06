ONE_SHOT = """Example survey:
<INTRODUCTION> Word2Vec is one of the most popular tools to learn word embeddings using shallow neural networks. It first constructs a vocabulary from the training text data and then learns word embeddings....
<HISTORY> Word2vec was developed by a group of researchers headed by Tomas Mikolov at Google. Machine learning models take vectors as input, ...
<KEY IDEAS> Word2Vec converts words into vector forms such that similar meaning words appear together and dissimilar words are located far away...
<USES/APPLICATIONS> Gensim provides the Word2Vec class for working with a Word2Vec model. Training your own word vectors can take a long time and uses lots of memory...
<VARIATIONS> Word embeddings is an active research area trying to figure out better word representations than the existing ones..."""

PROMPT = """Generate a Wikipedia-style survey about {topic}. There should be five sub-sections: Introduction, History, Key Ideas, Variations and Applications. Each sub-section should contain 50-150 words. The following is the guideline for each section:
SECTION 1: INTRODUCTION Describe what the topic is (a method, a model, a task, a dataset), which field/subfield it is part of, quick overview of applications and motivation behind concept and related ideas)
SECTION 2: HISTORY Describe when or by who the topic was introduced, in what context, what problems it addresses.
SECTION 3: KEY IDEAS Describe in greater depth (could provide some mathematical context or explain core concepts).
SECTION 4: USES/APPLICATIONS Describe for what tasks this model/data is used.
SECTION 5: VARIATIONS What variations or similar models, datasets, tasks exist and how does this topic fit into a bigger picture."""