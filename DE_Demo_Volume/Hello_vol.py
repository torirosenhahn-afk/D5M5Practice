from pathlib import Path
from datetime import datetime

out = Path("data/Hello.txt")

# Create the parent folder if it doesn't exist
out.parent.mkdir(parents=True, exist_ok=True)

with out.open("a") as f:
    f.write(f"Hello docker volume [{datetime.now()}]\n")

print(f"Written to {out.resolve()}")