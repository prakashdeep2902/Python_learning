from typing import Dict

badabhai: dict[str, int] = {"akash": 1}

chotaBhai: dict[str, int] = {"vikash": 4, "prakash": 5}

brothers: dict[str, int] = badabhai | chotaBhai

print(brothers)
