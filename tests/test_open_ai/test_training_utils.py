import pytest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))


from open_ai.training_utils import dataset_error_checks

def test_empty_dataset():
    """Test case 1: Empty dataset"""
    dataset = []
    assert dataset_error_checks(dataset) == []

def test_valid_dataset_no_errors():
    """Test case 2: Valid dataset with no errors"""
    dataset = [
        {
            "messages": [
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "How are you?"},
                {"role": "assistant", "content": "I'm good"}
            ]
        }
    ]
    assert dataset_error_checks(dataset) == []

def test_invalid_dataset_with_errors():
    """Test case 3: Invalid dataset with errors"""
    dataset = [
        {
            "messages": [
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "How are you?"},
                {"role": "assistant", "content": "I'm good"},
                {"role": "assistant", "content": "I'm great", "invalid_key": "value"} # Invalid key
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "What's your name?", "invalid_key": "value"}, # Invalid key
                {"role": "assistant", "content": "I don't have a name"},
                {"role": "assistant", "content": "I'm an AI assistant"} 
            ]
        },
        {
            "messages": [
                {"role": "system", "content": "Tell me a joke"},
                {"role": "user", "content": "Thank you"}  # Missing assistant message
            ]
        }
    ]
    expected_errors = [
        "message_unrecognized_key: 2",
        "example_missing_assistant_message: 1",
    ]
    
    assert dataset_error_checks(dataset) == expected_errors
