# encoding=utf-8
# 标记测试用例

import pytest
import random
import sys


class TestSequenceFunctions:
    def setup(self):
        self.seq = list(range(10))

    def teardown(self):
        pass

    @pytest.mark.run
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        assert self.seq == list(range(10))
        assert self.seq != (1, 2, 3)

    @pytest.mark.skip
    def test_choice(self):
        element = random.choice(self.seq)
        assert element in self.seq

    @pytest.mark.skipif(sys.platform.startswith("win"), reason="On Windows")
    def test_sample(self):
        for element in random.sample(self.seq, 5):
            assert element in self.seq
