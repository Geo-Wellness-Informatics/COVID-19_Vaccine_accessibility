# Evaluating Geographic Accessibility to COVID-19 Vaccination Across 54 Countries/Regions

## Key Findings

This comprehensive study evaluated geographic accessibility to COVID-19 vaccination sites across 54 countries/regions, revealing significant disparities in vaccine access:

- **Major disparities in accessibility**: In about 24% of studied countries/regions, over 95% of the population can access vaccination services within 15 minutes. However, in places like Manitoba (Canada), Zimbabwe, and Bhutan, less than 30% of the population can reach sites within 60 minutes.

- **"Vaccine deserts"**: Underserved areas were identified in both high-income countries (HICs) and low and middle-income countries (LMICs).

- **Correlation with outcomes**: Countries with higher vaccine accessibility tend to achieve higher vaccination rates, while those with lower accessibility often experienced higher COVID-19 mortality increases.

- **Economic factors**: A significant positive relationship was found between GDP per capita and vaccine accessibility (β=0.323, p<0.001).

## Methodology

Our analytical workflow begins with data collection through web scraping. The process starts with `scraping.py` and `USA_scraping.ipynb`, which gather the necessary vaccination site data and compile it into the `Vaccination_Site_dataset` directory.

Once we have collected the raw data, we process it through a series of analytical steps:

1. First, we organize the spatial data using `OSRM_KDTree.ipynb`, which calculates the Euclidean distances from each population center to all vaccination sites.

Next, we apply filtering criteria with `OSRM_filter.ipynb` to filter out vaccination sites that are located beyond a 100km straight-line distance threshold from population centers

3. The `OSRM_Distance_Calculation.ipynb` script calculates actual travel distances between population grids and vaccination sites using the Open Source Routing Machine (OSRM), providing crucial real-world accessibility metrics that account for road networks and geographic barriers.

4. We then implement the Enhanced Two-Step Floating Catchment Area (E2SFCA) methodology in `E2SFCA_manual_calculation.ipynb` to evaluate spatial accessibility to vaccination services. This  spatial analysis technique considers both supply (vaccination site capacity) and demand (population distribution) factors to generate comprehensive accessibility scores.

5. The analytical results are compiled into `Final_result.csv`, which contains the comprehensive accessibility scores for each population center, providing a quantitative basis for identifying underserved areas.

6. For deeper analysis of proximity factors, we use `Nearest_Score.ipynb` to calculate and visualize the closest vaccination sites to each population center, offering insights into minimum travel distances required to access vaccination services.

7. Finally, we visualize our findings with `Figure5_visualization.ipynb`, creating informative graphics that illustrate spatial accessibility patterns and potential service gaps. 

## Implications

- LMICs require enhanced attention to improve geographic accessibility to vaccination
- Internal disparities exist within both HICs and LMICs
- National public health officials should prioritize "vaccine deserts" 
- More equitable vaccine access planning is crucial for future pandemics

## Research Team

Yanjia Cao, Tianyu Li, Huanfa Chen, Qunshan Zhao, Jiashuo Sun, Karen Ann Grépin, Jeon-Young Kang

## 🔗 Links

- [Full Paper in BMJ Global Health](https://gh.bmj.com/content/10/2/e017761)
