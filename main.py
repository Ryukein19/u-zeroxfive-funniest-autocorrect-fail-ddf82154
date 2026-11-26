import os
# One-liner entry (under 200 chars): the line below is the entire submission.
# Output goes to /output/entry.txt.
LINE = "Told my boss I was 'ducking' excited for the launch. Autocorrect has now filed a formal complaint with HR on my behalf."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
