import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Load the data
df = pd.read_csv('Hyderabad_Heat_Data_Mission_0.csv').dropna()

# 2. Pick our "Questions" (Features) and "Answer" (Target)
X = df[['NDVI', 'NDBI']] # We use Greenery and Buildings to predict...
y = df['LST']            # ...the Heat!

# 3. Split data into "Study Material" and "Test Exam"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. BUILD THE PHYSICS-AWARE AI
# We tell the AI: "Trees MUST reduce heat (-1), Buildings MUST increase heat (1)"
model = XGBRegressor(monotone_constraints=(-1, 1)) 

# 5. TRAIN THE AI
print("AI is studying the heat patterns of Hyderabad...")
model.fit(X_train, y_train)

# 6. CHECK THE AI's SCORE
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print(f"\n--- AI Training Finished! ---")
print(f"On average, the AI is off by only {error:.2f}°C.")
print("The AI now understands Hyderabad's heat physics.")

# 7. SAVE THE BRAIN
model.save_model('heat_doctor_brain.json')
print("\nBrain saved as 'heat_doctor_brain.json'.")