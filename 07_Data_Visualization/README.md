# 07 — Insight-Driven Data Visualization

Exploratory visualization on the Titanic dataset using 13 plot types.

Every plot answers a question. Every title is a finding.

---

## Dataset

Seaborn's built-in Titanic dataset — 891 passengers, 15 features.

Cleaned down to 712 rows after dropping high-null and redundant columns.

## Key Findings

- **Survival was about wealth, not age.** First class passengers survived at 3x the rate of third class — fare was the real dividing line.
- **Third class was the youngest group, yet died the most.** Age gave no advantage when your lifeboat access was determined by your deck.
- **Fare and class are strongly negatively correlated (−0.55).** The higher your class number, the less you paid — and the less likely you were to survive.

## Plots Covered

`histplot` · `kdeplot` · `countplot` · `barplot` · `boxplot` · `violinplot` · `stripplot` · `scatterplot` · `regplot` · `heatmap` · `pairplot` · `FacetGrid`

## Structure

```
07_Data_Visualization/
├── data/
│   ├── raw/
│   └── processed/
│       └── titanic_cleaned.csv
├── notebooks/
│   └── my_notebook.ipynb
├── outputs/
│   └── figures/          # 12 saved plots
├── requirements.txt
└── README.md
```

## Stack

Python · Seaborn · Matplotlib
