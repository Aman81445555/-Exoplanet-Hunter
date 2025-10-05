# -Exoplanet-Hunter
# Exoplanet Hunter: An AI-Ready Data Pipeline

### NASA Space Apps Challenge 2025 - "A World Away"

---

## ## Project Summary

This project demonstrates a complete pipeline for processing raw astronomical data to find the faint signals of exoplanets. Our goal was to create a program that could take noisy data from space telescopes and produce clean, AI-ready data for planet discovery.

Faced with challenges in sourcing a suitable bulk dataset under the hackathon's time constraints, we pivoted our approach. Instead of training a new model, we focused on building a robust, live-data pipeline. This script successfully demonstrates the core technique by targeting the known exoplanet **Kepler-186f**. It programmatically downloads real mission data, cleans it, and processes it to visually confirm the planet's transit, proving the viability of our method.

---

## ## The Result

The script successfully generates a plot (`FINAL_Exoplanet_Transit_Plot.png`) showing a clean, "folded" light curve. The distinct dip in the center of the plot is the confirmed transit of Kepler-186f passing in front of its star.



This visual confirmation serves as a powerful proof-of-concept. The processed data is the ideal input for an AI/ML classification model, which represents the next step for this project.

---

## ## How It Works

1.  **Search & Download:** The script uses the `lightkurve` library to query NASA's Mikulski Archive for Space Telescopes (MAST) and download the light curve data for Kepler-186f.
2.  **Clean:** It removes outliers and bad data points from the raw brightness (flux) measurements.
3.  **Fold:** Using the known orbital period of Kepler-186f, the script "folds" the light curve. This technique stacks all the individual transit signals on top of one another, dramatically boosting the signal-to-noise ratio and making the faint transit visible.
4.  **Visualize:** Finally, it uses `matplotlib` to generate a plot of the folded light curve, saving it as a PNG image.

---

## ## Setup and Usage

**1. Prerequisites:**
* Python 3.x
* pip

**2. Installation:**
Clone the repository or download the files. Open a terminal in the project folder and install the required libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

**3. Running the Script:**
Execute the main script from your terminal:
```bash
python exoplanet_hunter.py
```
The script will run, download the necessary data, and generate the final plot `FINAL_Exoplanet_Transit_Plot.png` in the same directory.

---

## ## Tools and Data Sources

* **Language:** Python
* **Core Libraries:** `lightkurve`, `matplotlib`
* **Data Source:** NASA Mikulski Archive for Space Telescopes (MAST), specifically data from the Kepler Mission.
