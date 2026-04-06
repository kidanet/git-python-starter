from apps.wordcount import wordcount

def test_wordcount_basic():
    counts = wordcount("Git git! version control.")
    assert counts["git"] == 2
    assert counts["version"] == 1
    assert counts["control"] == 1
