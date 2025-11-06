from ligotools import readligo
import numpy as np
import pytest

def test_loaddata():
    """Test return data types for loaddata function."""
    values_loaddata = readligo.loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5")
    assert values_loaddata[0].dtype == np.float64
    assert values_loaddata[1].dtype == np.float64
    assert values_loaddata[2] is dict

def test_read_frame():
    """Test that read_frame raises a TypeError when ifo is None."""
    with pytest.raises(TypeError):
        readligo.read_frame("data/H-H1_LOSC_4_V2-1126259446-32.hdf5",ifo=None)