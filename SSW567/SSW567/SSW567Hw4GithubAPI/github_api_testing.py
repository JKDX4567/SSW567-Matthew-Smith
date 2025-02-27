import pytest
from unittest.mock import patch
from github_api import get_user_repos_commits

def test_get_user_repos_commits():
    # Mock repo requests
    mock_repos_response = [
        {'name': 'repo1'},
        {'name': 'repo2'}
    ]
    
    # Mock commit requests
    mock_commits_response_repo1 = [{'commit': {}}] * 10
    mock_commits_response_repo2 = [{'commit': {}}] * 5
    
    with patch('requests.get') as mock_get:
        # Set up mock responses
        mock_get.side_effect = [
            type('MockResponse', (), {'status_code': 200, 'json': lambda: mock_repos_response}),
            type('MockResponse', (), {'status_code': 200, 'json': lambda: mock_commits_response_repo1}),
            type('MockResponse', (), {'status_code': 200, 'json': lambda: mock_commits_response_repo2})
        ]
        
        result = get_user_repos_commits('testuser')
        
        assert result == [('repo1', 10), ('repo2', 5)]

def test_get_user_repos_commits_rate_limit():
    # Mock running out of calls
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.headers = {'X-RateLimit-Reset': 1234567890}
        
        #Supposed to get error here
        with pytest.raises(Exception) as exc_info:
            get_user_repos_commits('testuser')
        
        assert "Rate limit exceeded" in str(exc_info.value)

def test_get_user_repos_commits_user_not_found():
    # Mock not finding a user
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        
        #Also expects error
        with pytest.raises(Exception) as exc_info:
            get_user_repos_commits('nonexistentuser')
        
        assert "Couldn't find nonexistentuser" in str(exc_info.value)

def test_get_user_repos_commits_repo_commits_error():
    # Mock a repo response
    mock_repos_response = [{'name': 'repo1'}]
    
    # Mock commit error
    with patch('requests.get') as mock_get:
        mock_get.side_effect = [
            type('MockResponse', (), {'status_code': 200, 'json': lambda: mock_repos_response}),
            type('MockResponse', (), {'status_code': 404, 'json': lambda: None})
        ]
        
        #Also expects error
        with pytest.raises(Exception) as exc_info:
            get_user_repos_commits('testuser')
        
        assert "Failed to fetch commits for repository repo1" in str(exc_info.value)