from research_summary.utils.utils import json_to_object


def test_json_to_object():
    my_obg = json_to_object('{"language":"python"}')
    assert my_obg["language"] == "python"
