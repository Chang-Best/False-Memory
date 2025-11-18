import os
from gtts import gTTS


input_file = r"C:\Users\28718\Desktop\2024-2025\vanderbilt\PSY 4775 Human Memory\Chang Xu project\semantic_category_lists.txt"


output_dir = r"C:\Users\28718\Desktop\Word_sound"
os.makedirs(output_dir, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):

    line = line.strip()
    if not line or not line.startswith("*"):
        continue
    
    try:
        target, words_str = line[1:].split(":", 1)
    except ValueError:
        print(f"abnormal line: {line}")
        continue
    
    target = target.strip()
    words = [w.strip() for w in words_str.split(",") if w.strip()]
    
    # mp3
    for j, word in enumerate(words, start=1):
        tts = gTTS(text=word, lang="en")
        filename = f"List{i:02d}_{j:02d}_{word}.mp3"
        filepath = os.path.join(output_dir, filename)
        tts.save(filepath)
        print(f"saved: {filepath}")
