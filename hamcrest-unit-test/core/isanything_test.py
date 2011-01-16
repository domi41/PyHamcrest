__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isanything import anything

from matcher_test import MatcherTest


class IsAnythingTest(MatcherTest):

    def testAlwaysEvaluatesToTrue(self):
        assert_that(None, anything())
        assert_that(object(), anything())
        assert_that('hi', anything())

    def testHasUsefulDefaultDescription(self):
        self.assert_description('ANYTHING', anything())

    def testCanOverrideDescription(self):
        description = 'DESCRIPTION'
        self.assert_description(description, anything(description))

    def testMatchAlwaysSucceedsSoShouldNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(anything(), 'hi')


if __name__ == "__main__":
    unittest.main()
