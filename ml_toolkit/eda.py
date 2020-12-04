import numpy as np


def smooth1D(x_in, y_in, sigma=None, x_grid_size=100):
    
    """
    Gaussian smoother
    
    Example:
    x_g, y_hat = smooth1D(x, y, sigma=5)
    plt.plot(x, y, 'ro')
    plt.plot(x_g, y_hat, 'b-')
    """
    
    if type(x_in) is not np.ndarray:
        x_in = x_in.values
        y_in = y_in.values
    
    if sigma is None: sigma = np.std(x_in)
        
    def kernel(u, sigma):
        return np.exp(-u**2/(2*sigma**2))
    
    x_grid = np.linspace(min(x_in), max(x_in), 100)
    M = np.matrix([kernel(x_in-u, sigma) for u in x_grid])
    D = np.diag((1/np.sum(M, axis=1)).flatten().tolist()[0])
    
    return x_grid, np.dot(np.dot(D, M), y_in).tolist()[0]