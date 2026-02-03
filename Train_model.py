import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. DEFINE CATEGORIES
categories = ['E-commerce', 'Blog', 'Portfolio', 'Corporate', 'Food', 'Gaming', 'Education', 'Travel']

data = []

print("Generating 500 rows of synthetic design data...")

for _ in range(500):
    cat = random.choice(categories)
    
    # --- LOGIC RULES (Now with 3 Colors!) ---
    
    if cat == 'E-commerce':
        layout = 'Grid Layout'
        font = 'Roboto (Sans-Serif)'
        # High Energy Palette
        col_pri = '#FF5733 (Orange)'
        col_sec = '#2C3E50 (Dark Blue)'
        col_ter = '#ECF0F1 (Light Grey)'
        
    elif cat == 'Blog':
        layout = 'Single Column'
        font = 'Merriweather (Serif)'
        # Trustworthy Palette
        col_pri = '#3498DB (Blue)'
        col_sec = '#2980B9 (Darker Blue)'
        col_ter = '#FFFFFF (White)'
        
    elif cat == 'Portfolio':
        layout = 'Masonry'
        font = 'Playfair Display (Elegant)'
        # Creative Palette
        col_pri = '#2ECC71 (Green)'
        col_sec = '#27AE60 (Forest Green)'
        col_ter = '#F1C40F (Accent Yellow)'
        
    elif cat == 'Corporate':
        layout = 'Z-Pattern'
        font = 'Open Sans (Clean)'
        # Professional Palette
        col_pri = '#2980B9 (Classic Blue)'
        col_sec = '#BDC3C7 (Silver)'
        col_ter = '#2C3E50 (Charcoal)'
        
    elif cat == 'Food':
        # Smart Noise: Red vs White
        if random.random() < 0.8:
            layout = 'Split Screen'
            font = 'Poppins (Modern)'
            # Appetizing Red
            col_pri = '#E74C3C (Red)'
            col_sec = '#F1C40F (Cheese Yellow)'
            col_ter = '#27AE60 (Fresh Green)'
        else:
            layout = 'Minimalist Grid'
            font = 'Lato (Light)'
            # Clean White
            col_pri = '#FFFFFF (White)'
            col_sec = '#333333 (Dark Grey)'
            col_ter = '#E74C3C (Accent Red)'
            
    elif cat == 'Gaming':
        # Smart Noise: Cyberpunk vs Retro
        if random.random() < 0.7:
            layout = 'Dark Mode / Full Screen'
            font = 'Orbitron (Futuristic)'
            # Cyberpunk
            col_pri = '#8E44AD (Neon Purple)'
            col_sec = '#000000 (Pure Black)'
            col_ter = '#00FFFF (Cyan)'
        else:
            layout = 'Grid (Gallery View)'
            font = 'Press Start 2P (Pixel Art)'
            # Retro
            col_pri = '#2ECC71 (Neon Green)'
            col_sec = '#2C3E50 (Dark Blue)'
            col_ter = '#E74C3C (Pixel Red)'
        
    elif cat == 'Education':
        layout = 'F-Pattern (Readability)'
        font = 'Arial / Helvetica (Standard)'
        # Calm Palette
        col_pri = '#1ABC9C (Teal)'
        col_sec = '#ECF0F1 (Off White)'
        col_ter = '#F39C12 (Highlight Orange)'
        
    elif cat == 'Travel':
        layout = 'Hero Image Slider'
        font = 'Montserrat (Bold)'
        # Sunny Palette
        col_pri = '#F39C12 (Sun Yellow)'
        col_sec = '#3498DB (Ocean Blue)'
        col_ter = '#E67E22 (Sand)'
        
    data.append([cat, layout, font, col_pri, col_sec, col_ter])

# Create DataFrame
df = pd.DataFrame(data, columns=['Category', 'Layout', 'Font', 'Primary', 'Secondary', 'Tertiary'])

print("\nPreview of Data (With Full Palette):")
print(df.head(5)) 

# 2. ENCODE & TRAIN
df['Category_Code'] = df['Category'].astype('category').cat.codes
X = df[['Category_Code']]

# We now train 5 separate models!
print("\nTraining 5 Models...")
model_layout = RandomForestClassifier().fit(X, df['Layout'])
model_font = RandomForestClassifier().fit(X, df['Font'])
model_pri = RandomForestClassifier().fit(X, df['Primary'])
model_sec = RandomForestClassifier().fit(X, df['Secondary'])
model_ter = RandomForestClassifier().fit(X, df['Tertiary'])

# 3. SAVE BRAINS
with open('model_layout.pkl', 'wb') as f: pickle.dump(model_layout, f)
with open('model_font.pkl', 'wb') as f: pickle.dump(model_font, f)
with open('model_pri.pkl', 'wb') as f: pickle.dump(model_pri, f)
with open('model_sec.pkl', 'wb') as f: pickle.dump(model_sec, f)
with open('model_ter.pkl', 'wb') as f: pickle.dump(model_ter, f)

print("\nSuccess! Full Design System Trained.")