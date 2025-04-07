import os
import requests
from pathlib import Path

# Create skills directory if it doesn't exist
skills_dir = Path("images/skills")
skills_dir.mkdir(parents=True, exist_ok=True)

# Dictionary of skill names and their logo URLs
skill_logos = {
    "python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "sql": "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg",
    "pyspark": "https://raw.githubusercontent.com/apache/spark-website/asf-site/content/images/spark-logo-trademark.png",
    "databricks": "https://www.databricks.com/wp-content/uploads/2021/10/db-nav-logo.svg",
    "hadoop": "https://raw.githubusercontent.com/devicons/devicon/master/icons/apache/apache-original.svg",
    "powerbi": "https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png",
    "aws": "https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
    "azure": "https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg",
    "mysql": "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg",
}

# Download each logo
for skill, url in skill_logos.items():
    file_path = skills_dir / f"{skill}.png"
    
    # Skip if file already exists
    if file_path.exists():
        print(f"Skipping {skill}.png - already exists")
        continue
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Save the image
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded {skill}.png")
    except Exception as e:
        print(f"Error downloading {skill}.png: {e}")

print("Download complete!")
