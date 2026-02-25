## Significant Disadvantages of Designer's Intelligence
- Time consuming for the designer
- Restricts capabilities, especially in unseen scenarios
# Abstract Learning Agent
- That precepts are used not just for choosing actions, but also for improving future performance
- 4 basic components:
	- Performance
		- Responsible for choosing actions known to offer good outcomes
		- Corresponds to the agents discussed earlier
	- Learning
		- Responsible for improving the performance element
		- Requires feedback
	- Critic
		- Responsible for providing feedback
		- Compares outcomes with objective performance standards from outside the agent
	- Problem Generator
		- Responsible for generating new experience
		- Requires exploration
## Types of Feedback
- Supervised learning: agent observes input-output pairs and learns a function that maps from input to output
- Unsupervised learning: agent learns patterns in the input without any explicit feedback 
- Reinforcement learning: agent learns from a series of reinforcements (rewards or punishments)
## Classification vs. Regression
- Classification = output is one of a finite set of values
- Regression = output is a number
## Training vs. Test Data
- Training set = data used to train the model
- Validation set = data used to tune or select model
- Testing set = unseen data used to evaluate model
## Underfitting vs. Overfitting
- Underfitting:
	- Poor fit on training data
	- Not generalise to unseen data
	- Model is too simple
- Ideal:
	- Good fit on training data
	- Generalise to unseen data
	- Model is balanced
- Overfitting: (gap between training and testing is huge)
	- Perfect fir
	- Not generalise to unseen data
	- Model too complex
## Performance Metrics
- Performance matrix: true positive, false negative, etc
- Accuracy: $$\frac{TP+TN}{TP+FP+TN+FN}$$
- Precision: $$\frac{TP}{TP+FP}$$
- Recall: (Correct positive predictions out of the actual positive samples) $$\frac{TP}{TP+FN}$$
- F-Score: (Harmonic mean of precision and recall) $$\frac{2TP}{2TP+FP+FN}$$
# Decision Tree
- Tree representation of a function that maps a vector of attributes to an output value
- Input is a description of a situation
- Output can be a yes or no, etc
- Fully expressive, can be huge
- Given $n$ binary attributes
	- $2^n$ combinations
	- $2^{2^{n}}$ possible functions
- Two principal problems:
	- Much bigger than necessary
	- Cannot generalise from the training set
		- Tree has been overfitted
## Better Algorithm
- Basic idea is always choose the most important attribute first
	- Makes the most difference
	- Ideally splitting examples into all pos or all neg
## Entropy and Information Gain
- Entropy is the measure of the uncertainty $$H(X) = -\sum\limits_{x}p(x)logp(x)$$
- Information gain is the expected reduction of the entropy after branching on the attribute
# Transformer
- A type of deep neural network
## Language Modelling
- Autoregressive modelling is a method where the next value in a sequence is predicted based on previous values
- Language modelling is to learn the probability distribution of word sequences, uses preceding context
## Word Embedding Naïve
- One-hot encoding:
	- Length of vector is lexicon size
	- Each dimension corresponds to a word in the lexicon
## Word Embedding Better
- Learn word embedding
	- Distance between vectors reflects the sematic differences
- Vector can be more compact with fewer dimensions
## Self Attention
- Learns relationships among queries, keys and values
- Each input token is transformed to these things