# 🌌 Starburst and AGN galaxy Classification Using Deep Learning
## Author
This project was created by [Félix David Rizo Serrano](LinkedIn: Felix David Rizo Serrano).

This project focuses on the **automatic classification of galaxies** into two types:  
**AGN (Active Galactic Nuclei)** and **Starburst galaxies**, using spectroscopic data from the **Sloan Digital Sky Survey (SDSS)**.

We apply **1D Convolutional Neural Networks (CNNs)** to analyze galaxy spectra in FITS format, with the aim of supporting astrophysical research through automated and reliable classification.

---

## 📁 Project Structure

```
galaxy_classifier/
├── data/                           # FITS files with galaxy spectral data
├── src/                            # Source code and preprocessing scripts
│   ├── data_preprocessing.py       # Data preprocessing script
│   ├── data_preprocessing_utils.py # Helper functions for data preprocessing
│   ├── evaluation_and_visualization.py # Evaluation and visualization script
│   ├── prepare_data.py             # Script for data preparation
│   ├── training_model.py           # Model training script
├── confusion_matrix.png            # Confusion matrix visualization
├── notebook.ipynb                  # Jupyter Notebook for exploration and model testing
├── training_accuracy_loss.png      # Training accuracy and loss curves
├── requirements.txt                # List of required dependencies
└── README.md                       # Project documentation
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
