# coding=utf-8
# !/usr/bin/python3

import pyaudio
import wave

import matplotlib.pyplot as plt
import numpy as np

RATE = 44100
CHUNK = 2048  # RATE / number of updates per second


# ======================================================================================================================
# Setup graphics
# ======================================================================================================================
def configure_graphics():
    global ax1, ax2
    plt.ion()
    fig = plt.figure("Sinal Elétrico")
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)


# ======================================================================================================================
# Plot time domain
# ======================================================================================================================
def show_song_device(audio_handler):
    for i in range(audio_handler.get_device_count()):
        dev = audio_handler.get_device_info_by_index(i)
        print(i,  dev['name'], dev['maxInputChannels'])


# ======================================================================================================================
# Plot time domain
# ======================================================================================================================
def plot_signal_time(signal_temp):
    ax1.cla()
    ax1.plot(signal_temp)
    ax1.grid()
    # ax1.axis([0, CHUNK, -32768, 32767])  # 65536 = 2^16 bits
    ax1.axis([0, CHUNK, min(signal_temp), max(signal_temp)])
    ax1.set_xlabel("Sinal no tempo")


# ======================================================================================================================
# Plot frequency domain
# ======================================================================================================================
def plot_signal_frequency(signal_freq):
    array_freq = np.fft.rfftfreq(CHUNK, 1. / RATE)
    ax2.cla()
    ax2.plot(array_freq, signal_freq)
    ax2.grid()
    ax2.axis([0, 5000, 0, max(signal_freq)])
    ax2.set_xlabel("Sinal em frequencia")


# ======================================================================================================================
# Plot signals
# ======================================================================================================================
def plot_signal(data):
    signal_temp = np.array(wave.struct.unpack("%dh" % CHUNK, data)) * np.blackman(CHUNK)
    signal_freq = np.abs(np.fft.rfft(signal_temp))

    plot_signal_time(signal_temp)
    plot_signal_frequency(signal_freq)

    plt.pause(0.0001)


# ======================================================================================================================
# Main
# ======================================================================================================================
if __name__ == "__main__":

    p = pyaudio.PyAudio()
    # show_song_device(p)
    id_song_device = 1  # default -> USB Audio Device: - (hw:1,0) 2

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=id_song_device)

    configure_graphics()

    try:
        while 1:
            plot_signal(stream.read(CHUNK, exception_on_overflow=False))
    except:
        stream.stop_stream()
        stream.close()
        p.terminate()