import pytest
from hash_code.Y2021.practice_round.tools import format_input


@pytest.mark.parametrize("content,expected", [
    (
            [
                ['5', '1', '2', '1'],
                ['3', 'onion', 'pepper', 'olive'],
                ['3', 'mushroom', 'tomato', 'basil'],
                ['3', 'chicken', 'mushroom', 'pepper'],
                ['3', 'tomato', 'mushroom', 'basil'],
                ['2', 'chicken', 'basil']
            ],
            (
                    5,
                    1,
                    2,
                    1,
                    [
                        ['onion', 'pepper', 'olive'],
                        ['mushroom', 'tomato', 'basil'],
                        ['chicken', 'mushroom', 'pepper'],
                        ['tomato', 'mushroom', 'basil'],
                        ['chicken', 'basil']
                    ]
            )
    )
])
def test_format_content(content, expected):
    computed = format_input(content)
    assert computed == expected
