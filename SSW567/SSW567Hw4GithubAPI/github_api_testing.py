import unittest
from unittest.mock import patch
from github_api import get_user_repos_commits, print_repo_commit_count

class TestGitHubAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_repos_commits_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]       
        mock_get.side_effect = [
            type("MockResponse", (), {"status_code": 200, "json": lambda: [{"commit": {}}] * 10}),
            type("MockResponse", (), {"status_code": 200, "json": lambda: [{"commit": {}}] * 5})
        ]
        result = get_user_repos_commits("testuser")
        self.assertEqual(result, [("repo1", 10), ("repo2", 5)])

    @patch('requests.get')
    def test_get_user_repos_commits_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("nonexistentuser")
        self.assertTrue("Couldn't find nonexistentuser" in str(context.exception))

    @patch('requests.get')
    def test_get_user_repos_commits_rate_limit_exceeded(self, mock_get):
        mock_get.return_value.status_code = 403
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("testuser")
        self.assertTrue("Rate limit exceeded" in str(context.exception))
  
    @patch('requests.get')
    def test_get_user_repos_commits_repo_commits_error(self, mock_get):
        mock_get.side_effect = [
            type("MockResponse", (), {"status_code": 200, "json": lambda: [{"name": "repo1"}]}),
            type("MockResponse", (), {"status_code": 404, "json": lambda: None})
        ]
        with self.assertRaises(Exception) as context:
            get_user_repos_commits("testuser")
        self.assertTrue("Failed to fetch commits for repository repo1" in str(context.exception))

    @patch('requests.get')
    def test_print_repo_commit_count(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get.side_effect = [
            type("MockResponse", (), {"status_code": 200, "json": lambda: [{"commit": {}}] * 10}),
            type("MockResponse", (), {"status_code": 200, "json": lambda: [{"commit": {}}] * 5})
        ]
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            print_repo_commit_count("testuser")
        output = f.getvalue()
        expected_output = "Repo: repo1. Number of commits: 10.\nRepo: repo2. Number of commits: 5.\n"
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
