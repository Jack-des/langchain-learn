import json
def json_to_object(json_str):
    """Convert a JSON string to an object."""
    try:
        return json.loads(json_str)
    except Exception:
        return {}
