import pytest

from src.glue import extract, transform, load


class TestGlue:
    def test_extract(self):
        df = extract()
        assert df.shape == (3, 2)

    def test_transform(self):
        df = extract()
        df = transform(df)
        assert df.shape == (3, 3)

    def test_load(self):
        df = extract()
        df = transform(df)
        load(df)
        

