Status Report

**Overview**:  
This project investigates the relationship between environmental conditions and mental health by correlating air quality data with conversational data related to mental health. The objective is to investigate whether increased air pollution is linked to increased expressions of mental health distress in the forms of anxiety and depression. Through the use of structured pollution data and unstructured text conversations, this project employs data curation, integration, and analysis techniques to make correlations between the physical and mental environments we live in.

**Research Question(s):**  
- Is there a correlation between empirically measurable levels of air pollution and discussion frequency regarding mental health?  
- Are specific air pollutants (e.g., PM2.5, NO₂) more strongly associated with certain mental health themes like anxiety or depression?  
- Is the change in mental health conversation topics more pronounced in more polluted urban environments?

**Team**:  
As I am working alone, I am responsible for all programming and research tasks. This includes data profiling, cleaning, integration, analysis, workflow creation, documentation, and final reporting.

**Datasets:**  
Dataset 1: U.S. Air Quality Index (AQI) (CSV)  
- **Source:** [Kaggle: U.S. Pollution](https://www.kaggle.com/datasets/sogun3/uspollution)  
- **Description:** Contains daily air quality index readings for various pollutants (PM2.5, CO, O₃, NO₂, SO₂) across various U.S. cities between 2000 and 2016.  
- **Current Status:** Dataset has been downloaded and initial profiling is complete. Cleaning script (`scripts/clean_aqi.py`) is in progress.

Dataset 2: Mental Health Conversational Data (JSON)  
- **Source:** [Kaggle: Mental Health Conversational Data](https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data)  
- **Description:** Collection of mental health-themed discussions including FAQs, therapy cases, and user-advice discussions on depression and anxiety.  
- **Current Status:** Dataset downloaded. JSON loading and basic text cleaning script (`scripts/clean_convo.py`) is under development.

**Progress on Tasks:**  
- Data acquisition: Completed  
- Data profiling and quality checks: Completed  
- Data cleaning: In Progress  
- NLP topic extraction: Not Started  
- Data integration: Not Started  
- Visualization and correlation analysis: Not Started  
- Workflow automation (Snakemake): Not Started  
- Metadata and archiving: Not Started  

**Updated Timeline:**  
- **Mar 30–Apr 2**: Finalized project idea and datasets 
- **Apr 3–9**: Completed initial data profiling and quality checks 
- **Apr 10–15**: Began cleaning and preparing the JSON and CSV datasets (in progress)  
- **Apr 16–19**: (New estimate: May 3) NLP topic extraction  
- **Apr 20–23**: (New estimate: May 5) Integration of air quality and conversation datasets  
- **Apr 24–27**: (New estimate: May 7) Creation of visualizations and correlation analysis  
- **Apr 28–May 1**: (New estimate: May 8) Set up Snakemake workflow and reproducibility documentation  
- **May 1–6**: (New estimate: May 10) Archive project on Zenodo and add metadata + citations  

**Changes to Project Plan:**  
- Minor timeline adjustment: Due to the complexity of cleaning the mental health JSON data, subsequent steps have been pushed back by approximately one week.  
- Additional cleaning steps: Developing reusable scripts to automate cleaning rather than doing it manually, to ensure reproducibility.  
- Potential new analysis: If time permits, sentiment analysis may be added to better categorize anxiety vs. depression topics in conversations.

**Supporting Artifacts Committed:**  
- `StatusReport.md` — This interim report  
- `data/air_quality.csv` — Raw air quality data (accessed programmatically)  
- `data/mental_health.json` — Raw mental health conversation data (accessed programmatically)  
- `scripts/clean_aqi.py` — Initial cleaning script for air quality dataset  
- `scripts/clean_convo.py` — Initial cleaning script for mental health dataset  
- `Snakefile` — Starter file for workflow automation  
- `notebooks/data_profiling.ipynb` — Data profiling and inspection notebook  

**Next Steps:**  
- Complete data cleaning scripts  
- Begin NLP topic extraction from mental health conversations  
- Integrate cleaned datasets based on time and location  
- Perform correlation analysis and visualization  
- Finalize and automate the full workflow with Snakemake  
- Archive project on Zenodo with full metadata and reproducibility documentation

