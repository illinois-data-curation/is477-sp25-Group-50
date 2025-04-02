**Overview**: 
  This project investigates the relationship between environmental conditions and mental health by correlating air quality data with conversational data related to mental health. The objective is to investigate whether increased air pollution is linked to increased expressions of mental health distress in the forms of anxiety and depression. Through the use of structured pollution data and unstructured text conversations, this project employs data curation, integration, and analysis techniques to make correlations between the physical and mental environments we live in.

**Research Question(s):** 
    Is there a correlation between empirically measurable levels of air pollution and discussion frequency regarding mental health?
    Are specific air pollutants (e.g., PM2.5, NO₂) more strongly associated with certain mental health themes like anxiety or depression?
    Is the change in mental health conversation topics more pronounced in more polluted urban environments?
  
**Team**: 
    As I am working alone, I will be the sole person doing all programming and research for this project. I will be responsible for going over the data sets, sifting through them both by inspecting them virtually and through code. I will also be responsible for coming up with the final paper going over my conclusion of what I have found through this project.
    
**Datasets:** 
  Dataset 1: U.S. Air Quality Index (AQI) (CSV)
  - **Source:** [Kaggle: U.S. Pollution](https://www.kaggle.com/datasets/sogun3/uspollution)
  - **Description:** Contains daily air quality index readings for various pollutants (PM2.5, CO, O₃, NO₂, SO₂) across various U.S. cities between 2000 and 2016.
  - **Planned Use:** Will be filtered and aggregated by date and location to match conversational data timelines.
  
  Dataset 2: Mental Health Conversational Data (JSON)
  - **Source:** [Kaggle: Mental Health Conversational Data](https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data)
  - **Description:** Collection of mental health-themed discussions like FAQs, typical therapy cases, and user-advice discussions on depression and anxiety.
  - **Planned Use:** Data will be processed using JSON libraries to extract themes and frequency of mental health discussions. NLP tools will be used to label content by mental health themes and timeline.

**Timeline:** 
  - **Mar 30–Apr 2**: Finalized project idea and got both datasets
  - **Apr 3–9**: Did initial data profiling and quality checks
  - **Apr 10–15**: Cleaned and prepped the JSON (convo data) and CSV (AQI data)
  - **Apr 16–19**: Ran NLP on the convo data to extract topics + mental health terms
  - **Apr 20–23**: Integrated both datasets (pollution + convo themes) for analysis
  - **Apr 24–27**: Created visualizations and looked at correlations
  - **Apr 28–May 1**: Set up Snakemake workflow and wrote reproducibility docs
  - **May 1–6**: Archived project on Zenodo and added metadata + citations
