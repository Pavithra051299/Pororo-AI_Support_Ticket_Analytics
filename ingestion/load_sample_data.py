import pandas as pd

data = {
    "ticket_id": [1,2,3],
    "subject": ["Login issue","Payment failure","Bug report"],
    "priority": ["High","Medium","Low"]
}

df = pd.DataFrame(data)

print(df)