from unittest.mock import patch

import pytest

from todo_list import main


@pytest.fixture
def mock_main():
    with patch('builtins.print') as mock_print, patch(
        'builtins.input'
    ) as mock_input:
        yield mock_input, mock_print


def try_main(input_commands):
    try:
        main()
    except SystemExit:
        pass


def test_add(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['add Item1', 'quit']
    try_main(mock_input)
    mock_print.assert_any_call("Item 'Item1' added successfully")


def test_remove(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['add Item1', 'remove Item1', 'quit']
    try_main(mock_input)
    mock_print.assert_any_call("Item 'Item1' removed successfully")


def test_view(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['add Item1', 'view', 'quit']
    try_main(mock_input)
    mock_print.assert_any_call('Here is your todo list:', 'Item1', sep='\n- ')


def test_remove_non_existent_item(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['remove Item1', 'quit']
    try_main(mock_input)
    mock_print.assert_any_call("Item 'Item1' not found")


def test_add_duplicate_items(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['add Item1', 'add Item1', 'quit']
    try_main(mock_input)
    mock_print.assert_any_call("Item 'Item1' added successfully")


def test_large_volume_of_items(mock_main):
    mock_input, mock_print = mock_main
    mock_input.side_effect = ['add Item' + str(i) for i in range(1000)] + [
        'view',
        'quit',
    ]
    try_main(mock_input)
    mock_print.assert_any_call(
        'Here is your todo list:',
        *['Item' + str(i) for i in range(1000)],
        sep='\n- '
    )
