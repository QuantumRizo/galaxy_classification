# 🌌 Starburst and AGN galaxy Classification Using Deep Learning

This project focuses on the **automatic classification of galaxies** into two types:  
**AGN (Active Galactic Nuclei)** and **Starburst galaxies**, using spectroscopic data from the **Sloan Digital Sky Survey (SDSS)**.

We apply **1D Convolutional Neural Networks (CNNs)** to analyze galaxy spectra in FITS format, with the aim of supporting astrophysical research through automated and reliable classification.

---

## 📁 Project Structure

```
galaxy_classifier/
├── data/           # Contains the FITS files with galaxy spectral data
│   └── fits/       # Subdirectories for AGN and Starburst FITS files
├── models/         # Saved models after training
├── images/         # Plots and visualizations (e.g., training curves, confusion matrices)
├── src/            # Source code and Jupyter Notebooks for preprocessing and training
├── requirements.txt
└── README.md
```

---

## 🧠 Methodology

- **Input Data**: 1D flux arrays extracted from FITS files.
- **Model**: 1D Convolutional Neural Network (CNN) designed to capture spatial patterns in the spectra.
- **Preprocessing**: Spectra are resampled and normalized to a consistent shape.
- **Evaluation Metrics**: Accuracy, confusion matrix, and learning curves.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/galaxy-classification.git
cd galaxy-classification
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required libraries:**

- `tensorflow`
- `numpy`
- `astropy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---

## 📊 Results

- **Model Accuracy**: Over 90% on the validation set.
- **Confusion Matrix**: Shows strong performance distinguishing between AGN and Starburst galaxies.
- **Visualizations**: Learning curves and predictions help interpret model behavior and performance.

> The results demonstrate the effectiveness of deep learning in handling spectroscopic galaxy classification tasks, potentially accelerating large-scale galaxy analysis efforts.

---

## 🪐 About the Data

- The spectral data is sourced from SDSS in FITS format.
- Two galaxy types were used:
  - **AGN (Active Galactic Nuclei)**
  - **Starburst Galaxies**

---

## 🤝 Acknowledgments

- Sloan Digital Sky Survey (SDSS)
- Astropy and other scientific Python ecosystem tools
