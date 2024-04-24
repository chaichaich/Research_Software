"""Function that tests the sort."""

import os
import pytest
from litpack import utils

bs = '''{'first':3, 'last':1}'''

@pytest.fixture()
def setup():
    """Make then delete the bib file."""
    with open("test.bib", "w") as f:
        f.write(bs)
    yield "setup"
    os.unlink("test.bib")


class TestSort:
  """A Test class."""
  def test_sort(self, setup):
    bs = {'first':3, 'last':1}
    """Test function for sorting."""
    sort = utils.sort(bs)
    assert sort == {'last':1, 'first':3}



