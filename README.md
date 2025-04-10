# Galaxy Classification Using Machine Learning

This project uses machine learning techniques to classify galaxies into two categories: AGN (Active Galactic Nuclei) and Starburst galaxies. The classification is based on spectral data, processed from FITS files.

## Project Structure

- `data/`: Contains the FITS files with galaxy spectral data.
  - `fits/`: Subdirectories with FITS files for AGN and Starburst galaxies.
- `src/`: Source code directory, including the Jupyter Notebook for model training and evaluation.
- `models/`: Folder where the trained models will be saved.
- `images/`: Folder to store generated plots and images, such as training curves and confusion matrices.

## Requirements

To run this project, you'll need the following Python libraries:

- `tensorflow`
- `numpy`
- `astropy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can install the required dependencies using:

```bash
pip install -r requirements.txt
