"""
Product Manager Agent

Role: Translates user ideas into technical specifications.
"""

from typing import Dict, Any


class ProductManagerAgent:
    """
    Agent responsible for creating technical specifications from user ideas.
    """

    def __init__(self):
        self.system_prompt = """You are an expert Product Manager for a software company.

Your job is to:
1. Understand user ideas
2. Ask clarifying questions if needed
3. Write detailed technical specifications
4. Define clear success criteria

Format your specifications as:
- Project description
- Core requirements
- Technical constraints
- Success criteria
- Testing requirements
"""

    def create_spec(self, user_idea: str) -> str:
        """
        Create a technical specification from a user idea.

        Args:
            user_idea: Natural language project description

        Returns:
            Markdown-formatted specification

        TODO: Implement this method using an LLM API
        Hints:
        - Use the system_prompt to guide the LLM
        - Ask for clarification if idea is vague
        - Generate comprehensive but focused specs
        - Include edge cases and error handling
        """

        # YOUR CODE HERE
        raise NotImplementedError("ProductManagerAgent.create_spec not implemented")

    def clarify_requirements(self, user_idea: str) -> list[str]:
        """
        Generate clarifying questions if the idea is vague.

        TODO: Implement this method
        """

        # YOUR CODE HERE
        pass
