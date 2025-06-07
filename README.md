# Screen-Shot-Script

A simple Python script to automatically take periodic screenshots and save them with random filenames.

## Description

This script uses `pyautogui` to capture screenshots every 4 seconds and saves them as `.jpg` files in your specified directory. Each screenshot is saved with a randomly generated filename to prevent overwriting.

## Requirements

- Python 3.x
- `pyautogui` library

Install dependencies (if needed):

```bash
pip install pyautogui
```

## Usage

1. **Set the Save Directory:**
   
   In the script, replace the path in the line:
   ```python
   pic.save(f'C:/.../{x}.jpg')  # ... -> your address
   ```
   with the folder where you want your screenshots to be saved. Example:
   ```python
   pic.save(f'C:/Users/YourName/Pictures/Screenshots/{x}.jpg')
   ```

2. **Run the Script:**

   ```bash
   python your_script.py
   ```

   The script will start taking a screenshot every 4 seconds and save it in the specified directory.

## Note

- To stop the script, press `Ctrl+C` in the terminal.
- Make sure the save directory exists or create it before running the script.

## Disclaimer

This script will run indefinitely until stopped manually.
