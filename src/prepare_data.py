
import os
import numpy as np
import tensorflow as tf
from data_preprocessing import agn_sample, starburst_sample
from data_preprocessing_utils import interpolate_spectra

# Configure TensorFlow to suppress unnecessary log messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # '0' shows all logs, '1' shows warnings, '2' only errors, '3' disables logging entirely

# Disable additional CUDA-related warnings
tf.get_logger().setLevel('ERROR')  # Set TensorFlow logger to show only error messages  

# Interpolate the spectra to a target length
target_length = 2000  # Desired length for each spectrum
agn_flux = interpolate_spectra(agn_sample, target_length=target_length)
starburst_flux = interpolate_spectra(starburst_sample, target_length=target_length)

# Output the dimensions of the interpolated spectra to ensure correct shape
print(f"Dimensions of interpolated spectra: AGN = {agn_flux.shape}, Starburst = {starburst_flux.shape}")

# Identify valid spectra (those without NaN values)
agn_valid = ~np.isnan(agn_flux).any(axis=1)  # Check for NaN values across each spectrum (rows)
starburst_valid = ~np.isnan(starburst_flux).any(axis=1)  # Check for NaN values across each spectrum (rows)

# Filter out invalid spectra (those containing NaN values)
agn_flux = agn_flux[agn_valid]
starburst_flux = starburst_flux[starburst_valid]

# Output the number of valid spectra to verify the filtering process
print(f"Valid spectra: AGN = {agn_flux.shape}, Starburst = {starburst_flux.shape}")

# Subsample the Starburst data to match the number of AGN spectra
starburst_flux = starburst_flux[:2393]  # Ensure the number of Starburst spectra matches AGN

# Output the new size of the datasets after subsampling
print(f"New dataset size: AGN = {agn_flux.shape}, Starburst = {starburst_flux.shape}")

# Create labels: 0 for AGN, 1 for Starburst
agn_labels = np.zeros(agn_flux.shape[0])  # Labels for AGN (0)
starburst_labels = np.ones(starburst_flux.shape[0])  # Labels for Starburst (1)

# Concatenate the AGN and Starburst data
X = np.concatenate([agn_flux, starburst_flux], axis=0)  # Combine the spectra into one dataset

# Concatenate the corresponding labels
y = np.concatenate([agn_labels, starburst_labels], axis=0)  # Combine the labels into one array
