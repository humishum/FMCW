import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from math import ceil
from scipy.signal import find_peaks



config = {"f_c_hz": 10e9, "B_Hz": 500e6, "T_s": 500e-6, "target_distance_m": 10000}

f_c_hz = config.get("f_c_hz")  # Carrier Frequency (Hz)
B_Hz = config.get("B_Hz")  # Bandwidth (Hz)
T_s = config.get("T_s")  # Sweep Period(s)
target_distance_m = config.get("target_distance_m")  # Target Distance (m)
alpha = B_Hz / T_s  # Chirp Rate (rate of freq sweep)
tau_s = 2 * target_distance_m / 3e8  # round-trip delay
f_b_max = alpha * tau_s  # Maximum beat frequency(Hz)
fs_hz = f_b_max * 2.5  # Sampling Freq(Hz)


# Get global Time array
def generate_timescale(period_s, sampling_freq_hz, num_periods=1) -> npt.ArrayLike:
    num_samples = ceil(period_s * sampling_freq_hz * num_periods)
    return np.linspace(0, period_s * num_periods, num_samples, endpoint=False)


def phi_tx(t: np.ndarray, f_c_hz: float, alpha, a_sl=0, f_sl=0) -> np.ndarray:
    """Generate array of phase values, with optional error
    Args:
        t(np array): time array
        f_c_hz: carrier freq
        alpha: chirp rate
        a_sl_error: amplitudal error
        f_sl_error error
    """
    return 2 * np.pi * (f_c_hz * t + (1 / 2 * alpha * t**2)) + a_sl * np.sin(
        2 * np.pi * f_sl * t
    )


t = generate_timescale(period_s=T_s, sampling_freq_hz=fs_hz, num_periods=1)

# Get ideal TX and RX phase
s_tx = phi_tx(t, f_c_hz, alpha)
s_rx = phi_tx(t - tau_s, f_c_hz, alpha)

# Generate tx and rx phase with error
s_ni_tx = phi_tx(t, f_c_hz, alpha, 1, 40000)
s_ni_rx = phi_tx(t - tau_s, f_c_hz, alpha, 1, 40000)

# mix signals 
s_if = np.exp(1j * s_tx) * np.exp(-1j * s_rx)

# Estimate phase error in non-ideal TX and RX
# - moduular to use differnet methods of calculation and

# Apply PEC to non-ideal TX and RX
# - moduular to use differnet methods of calculation and


# Generate and save plot, with SNR metrics
