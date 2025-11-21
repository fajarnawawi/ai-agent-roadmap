"""
Developer Agent

Role: Implements code based on specifications.
"""

from typing import Tuple


class DeveloperAgent:
    """
    Agent responsible for writing code based on specifications.
    """

    def __init__(self):
        self.system_prompt = """You are an expert Python developer.

Your job is to:
1. Read technical specifications carefully
2. Write clean, well-documented Python code
3. Follow PEP 8 style guidelines
4. Include type hints
5. Handle errors gracefully
6. Write comprehensive test cases

Code requirements:
- Clear function and variable names
- Docstrings for all functions
- Error handling with try/except
- Edge case handling
- No hardcoded values
"""

    def write_code(self, specification: str, feedback: str = None) -> Tuple[str, str]:
        """
        Generate code and tests based on specification.

        Args:
            specification: Technical spec from Product Manager
            feedback: Optional feedback from Reviewer for fixes

        Returns:
            Tuple of (code, tests)

        TODO: Implement this method using an LLM API
        Hints:
        - Parse the specification carefully
        - If feedback is provided, focus on fixing those issues
        - Generate both application code and test code
        - Ensure code is complete and runnable
        """

        # YOUR CODE HERE
        raise NotImplementedError("DeveloperAgent.write_code not implemented")

    def fix_bugs(self, code: str, issues: list[str]) -> str:
        """
        Fix specific issues in code.

        TODO: Implement this method
        """

        # YOUR CODE HERE
        pass
