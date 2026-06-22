from datetime import date, datetime

letter = """
Dear <|Name|>  
you are selected for <|company|> date is <|date|>
"""

print(
    letter.replace("<|Name|>", "prakash")
    .replace("<|company|>", "Nobroker")
    .replace("<|date|>", str(datetime.today()))
)
