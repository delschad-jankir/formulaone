import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    """
    Class to encode decimal.Decimal objects as strings, so they can be written to a JSON file
    """
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

"""
# Example usage:
data = {
    "value1": Decimal("12.34"),
    "value2": Decimal("56.78"),
    "nested": {
        "value3": Decimal("90.12")
    }
}

json_data = json.dumps(data, cls=DecimalEncoder, indent=4)
print(json_data)
"""