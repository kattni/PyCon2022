"""
Theremin

    Andrew Kubera <github.com/akubera>

Use light-sensors to control the speaker with your hand.

Requires lighted room.
"""

import time
from adafruit_circuitplayground import cp

MAX_FREQ = 1200
MIN_FREQ = 400

# linear map of light fraction to frequency
SLOPE = (MIN_FREQ - MAX_FREQ) / LIGHT_THRESHOLD
INTERCEPT = MAX_FREQ

# if light above this threshold: no hand => no sound
LIGHT_THRESHOLD = 0.90

# depends on brightness in room?
MAX_SENSOR_LIGHT_LEVEL = 320.0


def read_normalized_light_value(duration_ms=1.5):
    """Take mean of light level after measuring for duration"""
    norm = 1 / MAX_SENSOR_LIGHT_LEVEL
    n = 1
    s = cp.light * norm
    t0 = time.monotonic_ns()
    while (time.monotonic_ns() - t0) < duration_ms * 1e6:
        s += cp.light * norm
        n += 1
    return s / n


def start_tone(frequency):
    """Use 'custom' start_tone to avoid clicks when changing frequencies."""
    if cp._sample is not None:
        cp._sample.stop()
    cp._speaker_enable.value = True
    length = 100
    if length * frequency > 350000:
        length = 350000 // frequency
    cp._generate_sample(length)
    # Start playing a tone of the specified frequency (hz).
    cp._sine_wave_sample.sample_rate = int(len(cp._sine_wave) * frequency)
    if not cp._sample.playing:
        cp._sample.play(cp._sine_wave_sample, loop=True)


prev_freq = 0
while True:
    light_percentage = read_normalized_light_value()

    # no noise if no hand detected (too bright)
    if light_percentage > LIGHT_THRESHOLD:
        if cp._sample is not None:
            cp._sample.stop()
        continue

    # calcuate frequency from light percentage
    freq = INTERCEPT + light_percentage * SLOPE

    # only change frequency if more than 5% difference
    freq_diff = abs(prev_freq - freq) / freq
    if freq_diff < 0.05:
        continue
    else:
        prev_freq = freq

    start_tone(freq)
