# UrbanHeat AI: Physics-Informed Geospatial System for Heat Mitigation

**Project for ISRO Bharatiya Antariksh Hackathon 2026**  
**Study Area:** Hyderabad, Telangana  
**Technology:** Geospatial AI, Remote Sensing (Landsat 8), XGBoost (Physics-Informed)

## 📋 Overview
This system identifies urban heat stress hotspots and simulates optimized cooling interventions. Unlike standard black-box ML models, UrbanHeat AI utilizes **monotone constraints** to ensure that predictions adhere to thermodynamic principles (e.g., increased vegetation must lead to temperature reduction).

## 🚀 Key Features
- **Module 1: Heat Hotspot Detection:** Multi-temporal LST mapping using Landsat 8 (TIRS) data.
- **Module 2: Driver Quantification:** Analyzes the contribution of NDBI (Urban Morphology) and NDVI (Vegetation) to heat stress.
- **Module 3: Physics-Informed AIML:** An XGBoost regressor built with physical constraints ($LST \propto NDBI$ and $LST \propto 1/NDVI$).
- **Module 4: Mitigation Optimizer:** Scenario-based simulator for urban greening and albedo (cool roof) interventions.

## 🛠️ Methodology
1. **Data Acquisition:** Extracting LST, NDVI, and NDBI from Landsat 8 via Google Earth Engine.
2. **Feature Engineering:** Normalizing indices to establish land-surface correlations.
3. **ML Training:** Training an XGBoost model with an MAE of ~1.62°C, validated against seasonal summer peaks.
4. **Optimization:** Greedy search for optimal placement of greenery to maximize cooling per hectare.

## 📊 Outcomes
- **Validated AI Model:** Capturing urban heat dynamics with high accuracy.
- **Cooling Scenarios:** Quantitative proof that a 20% increase in Hyderabad's tree cover can reduce surface temperatures by up to 2.2°C.
- **Strategy Report:** Prioritized intervention zones based on Heat Risk Levels.

## 💻 Setup
1. `pip install -r requirements.txt`
2. `streamlit run app.py`