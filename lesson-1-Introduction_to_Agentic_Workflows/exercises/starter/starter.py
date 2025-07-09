"""
Program Management Knowledge Agent - Starter Code

This program demonstrates two approaches to answering program management questions:
1. Using hardcoded knowledge
2. Using an LLM API

Complete the TODOs to build your knowledge agent.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# TODO: Initialize the OpenAI client if API key is available
# Hint: Use os.getenv() to get the API key from environment variables
load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1"
)

def get_hardcoded_answer(question):
    """
    Return answers to program management questions using hardcoded knowledge.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer to the question
    """
    # TODO: Convert question to lowercase for easier matching
    question = question.lower()
    
    # TODO: Implement responses for at least 5 common program management questions
    # Include questions about: Gantt charts, Agile, sprints, critical path, and 
    if(question ==  'What is the weather'.lower()):
        return 'It is sunny'
    if(question == 'tell me a short joke'.lower()):
        return 'knock knock'
    return "unknown question"
    
    # TODO: Add a default response for questions not in your knowledge base
    pass

def get_llm_answer(question):
    """
    Get answers to program management questions using an LLM API.
    
    Args:
        question (str): The question about program management
        
    Returns:
        str: The answer from the LLM
    """
    # TODO: Check if the LLM client is 
    if(not client.api_key):
        return "client not initialized"
    
    # TODO: Implement the API call to get an answer from the LLM
    # Use a system message to specify that the LLM should act as a program management expert
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system","content": "you are a useful assistant"},
                {"role": "user","content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "unexpected error"


    
# Demo function to compare both approaches
def compare_answers(question):
    """Compare answers from both approaches for a given question."""
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    # TODO: Get and display the hardcoded answer
    print("**** Hardcoded Answer ****")
    print(get_hardcoded_answer(question))
    print("**** LLM Answer ****")
    print(get_llm_answer(question))
    
    # TODO: Get and display the LLM answer (or a placeholder message)
    
    print("=" * 50)

# Demo with sample questions
if __name__ == "__main__":
    print("PROGRAM MANAGEMENT KNOWLEDGE AGENT DEMO")
    print("=" * 50)
    
    # TODO: Create a list of sample program management questions
    questions = ['What is the weather', 'tell me a short joke']
    
    # TODO: Loop through the questions and compare answers
    for question in questions:
        compare_answers(question)

