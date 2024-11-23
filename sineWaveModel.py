import numpy as np
import matplotlib.pyplot as plt


def generate_sine_wave(amplitude=1.0, frequency=1.0, duration=1.0, sample_rate=1000, phase=0):
    """
    Generate a sine wave based on given parameters.

    Parameters:
    - amplitude: Amplitude of the sine wave.
    - frequency: Frequency of the sine wave in Hz.
    - duration: Duration of the wave in seconds.
    - sample_rate: Number of samples per second.
    - phase: Phase shift in radians.

    Returns:
    - t: Time array.
    - y: Sine wave values.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, y


def plot_sine_wave(amplitude=1.0, frequency=1.0, duration=1.0, sample_rate=1000, phase=0):
    """
    Plot a sine wave using matplotlib.

    Parameters are the same as generate_sine_wave.
    """
    t, y = generate_sine_wave(amplitude, frequency, duration, sample_rate, phase)
    plt.plot(t, y)
    plt.title(f"Sine Wave: {frequency} Hz, {amplitude} Amplitude")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example usage: Plot a sine wave with default parameters
    plot_sine_wave(amplitude=1.0, frequency=5.0, duration=1.0)
