# Evaluating Geographic Accessibility to COVID-19 Vaccination Across 54 Countries/Regions

## Study Overview
This research provides the first multicountry analysis comparing COVID-19 vaccination accessibility across both high-income countries (HICs) and low and middle-income countries (LMICs), revealing critical disparities in access and their relationship to health outcomes.

## Key Findings
- **Access Disparities**: In 24% of studied regions, >95% of the population can access vaccination within 15 minutes, while in Manitoba (Canada), Zimbabwe, and Bhutan, <30% can reach sites within 60 minutes
- **Economic Correlation**: Strong positive relationship between GDP per capita and vaccine accessibility (β=0.323, p<0.001)
- **Health Outcomes**: Higher accessibility correlates with increased vaccination rates (β=0.139, p<0.01)
- **"Vaccine Deserts"**: Identified in both HICs and LMICs, creating vulnerable populations

## Methodology & Data Processing Workflow

### 1. Data Collection
- Web scraping using `scraping.py` and `USA_scraping.ipynb`
- Population data (1km resolution) from WorldPop
- Vaccination site geocoding from health department websites

### 2. Spatial Analysis Pipeline
1. **Euclidean Distance Calculation** (`OSRM_KDTree.ipynb`)
   - Creates k-dimensional tree structure
   - Calculates straight-line distances between population centers and vaccination sites

2. **Distance Filtering** (`OSRM_filter.ipynb`)
   - Filters out vaccination sites beyond 100km threshold

3. **Travel Time Calculation** (`OSRM_Distance_Calculation.ipynb`)
   - Uses Open Source Routing Machine (OSRM)
   - Calculates real-world driving times on road networks

4. **Accessibility Scoring** (`E2SFCA_manual_calculation.ipynb`)
   - Implements Enhanced Two-Step Floating Catchment Area method
   - Considers both supply (vaccination capacity) and demand (population)

5. **Results Compilation** (`Final_result.csv`)
   - Comprehensive accessibility scores
   - Identifies underserved areas

6. **Proximity Analysis** (`Nearest_Score.ipynb`)
   - Analyzes closest vaccination sites to population centers
   - Calculates minimum travel distances

7. **Visualization** (`Figure5_visualization.ipynb`)
      - Correlation between accessibility and GDP per capita
      - Relationship between accessibility and vaccination rates
      - Analysis of accessibility impact on COVID-19 mortality 

## Research Team
Yanjia Cao, Tianyu Li, Huanfa Chen, Qunshan Zhao, Jiashuo Sun, Karen Ann Grépin, Jeon-Young Kang

## 🔗 Publication
[Full Paper in BMJ Global Health](https://gh.bmj.com/content/10/2/e017761)
