#!/usr/bin/env python3
import os

# Create 44 .txt and 44 .html placeholder files for Mystery Babylon episodes
for i in range(1, 45):  # Episodes 1 to 44
    episode_num = f"{i:02d}"  # Pad with leading zero (01, 02, ..., 44)
    txt_file = f"Episode_{episode_num}.txt"
    html_file = f"Episode_{episode_num}.html"

    # Skip if both files exist
    if os.path.exists(txt_file) and os.path.exists(html_file):
        print(f"Skipping Episode_{episode_num}: Files already exist")
        continue

    # Create .txt placeholder
    with open(txt_file, 'w') as f:
        f.write(f"Placeholder for Episode {episode_num} summary.")

    # Create .html placeholder
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mystery Babylon: Episode {episode_num}</title>
</head>
<body>
  <h1>Mystery Babylon: Episode {episode_num}</h1>
  <p>Placeholder content for Episode {episode_num}.</p>
</body>
</html>"""
    with open(html_file, 'w') as f:
        f.write(html_content)

    print(f"Created {txt_file} and {html_file}")

# Count total files created
file_count = len([f for f in os.listdir('.') if f.endswith(('.txt', '.html'))])
print(f"File creation complete. Total files: {file_count}")
