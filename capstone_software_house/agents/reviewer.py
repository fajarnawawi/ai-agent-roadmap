"""
Reviewer Agent

Role: Tests code and provides feedback.
"""

from typing import Dict, Any
import subprocess
import tempfile
from pathlib import Path


class ReviewerAgent:
    """
    Agent responsible for testing and reviewing code quality.
    """

    def __init__(self):
        self.system_prompt = """You are an expert code reviewer and QA engineer.

Your job is to:
1. Execute the code safely
2. Run all tests
3. Check for errors and bugs
4. Verify edge cases are handled
5. Assess code quality
6. Provide actionable feedback

Review criteria:
- Does the code run without errors?
- Do all tests pass?
- Are edge cases handled?
- Is error handling present?
- Is the code well-documented?
- Does it meet the specification?
"""

    def review(self, code: str, tests: str, spec: str) -> Dict[str, Any]:
        """
        Review code by executing and testing it.

        Args:
            code: Application code to review
            tests: Test code
            spec: Original specification

        Returns:
            Dictionary with:
            - approved: bool
            - issues: list of problems found
            - test_results: output from running tests
            - suggestions: improvement recommendations
            - score: 0-10

        TODO: Implement this method
        Hints:
        - Execute code safely (use subprocess with timeout)
        - Run tests and capture output
        - Check for syntax errors
        - Use LLM to assess quality against spec
        """

        # YOUR CODE HERE
        raise NotImplementedError("ReviewerAgent.review not implemented")

    def _execute_code_safely(self, code: str) -> Dict[str, Any]:
        """
        Execute code in a safe environment.

        TODO: Implement safe code execution
        Hints:
        - Use tempfile for isolation
        - Set timeout to prevent infinite loops
        - Capture stdout and stderr
        - Handle exceptions
        """

        # YOUR CODE HERE
        pass

    def _run_tests(self, code: str, tests: str) -> Dict[str, Any]:
        """
        Run test suite and return results.

        TODO: Implement test execution
        """

        # YOUR CODE HERE
        pass
