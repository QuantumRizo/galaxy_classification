
import numpy as np

def interpolate_spectra(data, target_length):
    """
    Interpolates spectra to adjust them to a fixed length.
    
    Args:
        data (list): List of tuples (loglam_rest, flux).
        target_length (int): The number of points to which each spectrum should be interpolated.
    
    Returns:
        np.ndarray: Array of interpolated spectra (flux).
    """
    interpolated_flux = []
    
    # Loop through each spectrum and apply linear interpolation
    for loglam_rest, flux in data:
        # Generate a uniform linear space for interpolation
        x_new = np.linspace(loglam_rest.min(), loglam_rest.max(), target_length)
        flux_interp = np.interp(x_new, loglam_rest, flux)  # Linear interpolation
        interpolated_flux.append(flux_interp)
    
    return np.array(interpolated_flux)
