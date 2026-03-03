# General Agents
### Definition
- AI systems that interact with environments through sensors and actuators
### Traditional Agents: Logical and Neural Agents
- What makes a Bokoblin an agent?
	- Link's status is the environment and what the Bokoblin interacts with
### Logical Agents
![[Pasted image 20251016141644.png]]
- Input is Link's position
- Rules is: weapon attack if close, arrow attack if far, get back to origin if Link too far away
- You can't list everything with prior knowledge. Therefore:
### Neural Agents
![[Pasted image 20251016141936.png]]
- Better perception and more complex logic

## Language Agent
- AI systems that interact with environments with LLMs through natural language as both sensors and actuators
- LLMS:
	- Huge AI models to predict next words
	- Powerful as it is trained with "all" the sentences in the world

## Open AI Operator
- Go to website and do action

## Language Agents vs. Traditional Agents
- If your tool is having some impact to the environment then it can be defined as an agent
- Logical Agent
	- Low expressiveness (bounded by the logical language)
	- Logical inferences for reasoning (sound, explicit, rigid)
	- Low adaptivity (bounded by knowledge curation)
- Neural Agent
	- Medium expressiveness (anything a small NN can encode)
	- Parametric inferences for reasoning (stochastic, implicit, rigid)
	- Medium adaptivity (data driven but sample inefficient)
- Language Agent
	- High expressiveness (almost anything)
	- Language based inferences for reasoning (fuzzy, semi-explicit, flexible)
	- High adaptivity (strong prior from LLMs and language use)

# Hallucination
- Uses past knowledge, but gets mixed up with current context

## LLMs with Retrieval Augmented Generation (RAG)
![[Pasted image 20251016144134.png]]
- LLMs with RAG retrieves context from knowledge base before taking actions
- Generally, agents also writes to knowledge base

# 3 Fundamental Pillars of Language Agents
![[Pasted image 20251016145410.png]]
## Reasoning
- Letting your agent analyse information and modify given prompts
- Adding a reasoning process to allow for the LLM to figure out how to get to the correct answer, drives the final answer via intermediate steps
- Self-reflection is also deemed as reasoning and quite helpful for language agents
![[Pasted image 20251016150846.png]]

## Planning
- Critical capability of language agents that are boosted by reasoning and memory

## Memory
![[Pasted image 20251016150913.png]]
- Read and write long-term memory to enrich context
- Episodic, Semantic and Procedure
	- Episodic: Direct observations
		- Rank recency or importance etc.
	- Semantic: Reflections (reasoning) derived from observations
	- Procedure: Store a set of procedures (encode multiple actions, generated tokens into one memory)

# Emerging Topics in Language Agents
- Supervised Fine-tuning in Agentic:
	- Gathering Traces
	- Agents learn sentence completion
- Reinforcement Learning in Agentic:
	- Gathering traces from agent itself
	- Optimise agent to get higher rewards