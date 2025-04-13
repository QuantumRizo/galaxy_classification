
import os
import numpy as np
from astropy.io import fits
from data_preprocessing_utils import interpolate_spectra

def process_fits_files(folder):
    """
    Processes FITS files in a directory to correct for redshift.
    
    Args:
        folder (str): Path to the directory containing FITS files.
    
    Returns:
        list: A list of tuples (loglam_rest, flux) for each file.
    """
    processed_data = []
    
    # Iterate over the files in the provided directory
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        
        # Skip files that do not have a .fits extension
        if not file_path.endswith('.fits'):
            continue
        
        # Open the FITS file and extract data
        with fits.open(file_path) as hdul:
            data = hdul[1].data  # Assuming data is in the second extension
            
            # Extract the relevant columns: loglam, flux, and redshift
            loglam = data['loglam']
            flux = data['flux']
            redshift = data['redshift']
            
            # Apply redshift correction to bring data to rest-frame
            loglam_rest = loglam - np.log10(1 + redshift)
            
            # Store the processed data
            processed_data.append((loglam_rest, flux))
    
    return processed_data

# Directories containing the FITS files (relative to the 'src' folder)
agn_dir = '../data/fits/agn_fits'
starburst_dir = '../data/fits/starburst_fits'

# Process the FITS files from each directory
agn_data = process_fits_files(agn_dir)
starburst_data = process_fits_files(starburst_dir)  # Select the first 'n' spectra from each dataset
num_samples = 2500

# Ensure that we do not exceed the total number of available spectra
agn_sample = agn_data[:num_samples] if len(agn_data) >= num_samples else agn_data
starburst_sample = starburst_data[:num_samples] if len(starburst_data) >= num_samples else starburst_data

# Log the number of selected spectra for both AGN and Starburst datasets
print(f"Number of spectra selected: {len(agn_sample)} AGN, {len(starburst_sample)} Starburst")
