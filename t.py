from __future__ import annotations
import numpy as np
import hist
from hist import Hist

def T(self) -> Self:
    return self.project(*reversed(range(self.ndim)))
    

def test_T_property():
    # Create a 2D histogram with some data
    hist_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    hist = hist_data

    # Accessing .T property to flip the axes
    hist_T = hist.T

    # Check that the axes are flipped correctly
    assert np.all(hist_T == np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))


    # Test 2 with a different 2D histogram
    hist_data_2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    hist_2 = hist_data_2
    hist_T_2 = hist_2.T
    assert np.all(hist_T_2 == np.array([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))

    # Test 3 with an empty histogram (should return an empty histogram)
    hist_empty = np.array([])
    hist_T_empty = hist_empty.T
    assert np.all(hist_T_empty == hist_empty)

    # Test 4 with negative values in the histogram
    hist_data_negative = np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
    hist_negative = hist_data_negative
    hist_T_negative = hist_negative.T
    assert np.all(hist_T_negative == np.array([[-1, -4, -7], [-2, -5, -8], [-3, -6, -9]]))
    
