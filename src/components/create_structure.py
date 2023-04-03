import os

# List of directories and files to create
components = [
    ("Header", ["Header.css", "Header.js"]),
    ("TeslaCar", ["TeslaCar.css", "TeslaCar.js"]),
    ("TeslaClimate", ["TeslaClimate.css", "TeslaClimate.js"]),
    ("TeslaCounter", ["TeslaCounter.css", "TeslaCounter.js"]),
    ("TeslaNotice", ["TeslaNotice.css", "TeslaNotice.js"]),
    ("TeslaStats", ["TeslaStats.css", "TeslaStats.js"]),
    ("TeslaWheels", ["TeslaWheels.css", "TeslaWheels.js"]),
]

# Iterate through the list and create directories and files
for directory, files in components:
    os.makedirs(directory, exist_ok=True)
    for file in files:
        with open(os.path.join(directory, file), "w") as f:
            pass

print("Directories and files created successfully.")
