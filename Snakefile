rule all:
    input:
        [
<<<<<<< HEAD
            "data/air_quality_clean.csv",
            "data/mental_health.json",
            "figures/air_quality_trends.png",
            "figures/mental_health_plot.png"
        ]

rule clean_air_quality:
    input: "data/pollution_us_2000_2016.csv"
    output: "data/air_quality_clean.csv"
    script: "scripts/clean_aqi.py"

rule clean_mental_health:
    input: "data/mental_health.json"
    output: "data/mental_health.json"
    shell: "cp {input} {output}"  # if no cleaning is needed

rule plot_air_quality:
    input: "data/air_quality_clean.csv"
    output: "figures/air_quality_trends.png"
    script: "scripts/plot_air_quality.py"

rule plot_mental_health:
    input: "data/mental_health.json"
    output: "figures/mental_health_plot.png"
    script: "scripts/plot_mental_health.py"
=======
            "data/air_quality.csv",
            "data/mental_health.json"
        ]
>>>>>>> 1aabb85ded670e9e4414539e7772aec17a257f69
