from ligotools.utils import utils
from ligotools import readligo as rl
import numpy as np
import os

def test_whiten_shape():
    np.random.seed(0)
    strain = np.random.randn(4096)

    # mock PSD function
    interp_psd = lambda f: np.ones_like(f)
    
    dt = 1/4096. 
    w = utils.whiten(strain, interp_psd, dt)
    assert w.shape == strain.shape

def test_write_wavfile():
    fs = 4096
    data = np.random.randn(4096)
    
    audio_folder = 'audio/'
    eventname = 'test' 
    filename = audio_folder + eventname+".wav"

    utils.write_wavfile(filename, fs, data)
    assert os.path.exists(filename)