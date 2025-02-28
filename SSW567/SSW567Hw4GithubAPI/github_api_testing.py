import unittest
from unittest.mock import patch, Mock
from github_api import get_user_repos_commits, print_repo_commit_count

class TestGitHubAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_repos_commits_success(self, mock_get):
        # Mock the repositories response
        mock_repos_response = Mock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [
            {"name": "repo1", "full_name": "testuser/repo1"},
            {"name": "repo2", "full_name": "testuser/repo2"}
        ]

        # Mock the commits responses
        mock_commits_response_1 = Mock()
        mock_commits_response_1.status_code = 200
        mock_commits_response_1.json.return_value = [{"commit": {}}] * 10

        mock_commits_response_2 = Mock()
        mock_commits_response_2.status_code = 200
        mock_commits_response_2.json.return_value = [{"commit": {}}] * 5

        # Set up side_effect to return the mocked responses in order
        mock_get.side_effect = [
            mock_repos_response,
            mock_commits_response_1,
            mock_commits_response_2
        ]

        # Call the function
        result = get_user_repos_commits("testuser")

        # Assert the results
        self.assertEqual(result, [("repo1", 10), ("repo2", 5)])

    @patch('requests.get')
    def test_get_user_repos_commits_user_not_found(self, mock_get):
        # Mock a 404 error for user not found
        mock_get.return_value.status_code = 404

        # Call the function and expect an exception
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("nonexistentuser")

        # Assert the error message
        self.assertTrue("Couldn't find nonexistentuser" in str(context.exception))

    @patch('requests.get')
    def test_get_user_repos_commits_rate_limit_exceeded(self, mock_get):
        # Mock a 403 error for rate limiting
        mock_get.return_value.status_code = 403

        # Call the function and expect an exception
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("testuser")

        # Assert the error message
        self.assertTrue("Rate limit exceeded" in str(context.exception))

    @patch('requests.get')
    def test_get_user_repos_commits_repo_commits_error(self, mock_get):
        # Mock the repositories response
        mock_repos_response = Mock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [{"name": "repo1", "full_name": "testuser/repo1"}]

        # Mock a 404 error for the commits response
        mock_commits_response = Mock()
        mock_commits_response.status_code = 404

        # Set up side_effect to return the mocked responses in order
        mock_get.side_effect = [
            mock_repos_response,
            mock_commits_response
        ]

        # Call the function and expect an exception
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("testuser")

        # Assert the error message
        self.assertTrue("Failed to fetch commits for repository repo1" in str(context.exception))

    @patch('requests.get')
    def test_print_repo_commit_count(self, mock_get):
        # Mock the repositories response
        mock_repos_response = Mock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [
            {"name": "repo1", "full_name": "testuser/repo1"},
            {"name": "repo2", "full_name": "testuser/repo2"}
        ]

        # Mock the commits responses
        mock_commits_response_1 = Mock()
        mock_commits_response_1.status_code = 200
        mock_commits_response_1.json.return_value = [{"commit": {}}] * 10

        mock_commits_response_2 = Mock()
        mock_commits_response_2.status_code = 200
        mock_commits_response_2.json.return_value = [{"commit": {}}] * 5

        # Set up side_effect to return the mocked responses in order
        mock_get.side_effect = [
            mock_repos_response,
            mock_commits_response_1,
            mock_commits_response_2
        ]

        # Call the function and capture the output
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            print_repo_commit_count("testuser")
        output = f.getvalue()

        # Assert the output
        expected_output = "Repo: repo1. Number of commits: 10.\nRepo: repo2. Number of commits: 5.\n"
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
