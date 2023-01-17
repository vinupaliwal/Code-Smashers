import streamlit as st
import base64
import numpy as np
from scipy.io import wavfile  
from wavfile import  read, write
from scipy.fftpack import fft, ifft
import numpy as np
import IPython
import wave
import struct
import matplotlib.pyplot as plt
from scipy import fftpack

st.set_page_config(page_title='Code Smashers', layout="wide")

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

st.title('Code Smashers')

col1, col2, col3 = st.columns([3,2,2])

with col1:
    st.header("Upload file")
    uploaded_file = st.file_uploader("Upload file",label_visibility="collapsed")
    audiofile =  uploaded_file
    IPython.display.Audio(audiofile)
    from pydub import AudioSegment
    file_extension = 'mp3'
    track = AudioSegment.from_file(audiofile, file_extension)
    audiofile_wave = audiofile.replace(file_extension, 'wav')
    file_handle = track.export(audiofile_wave, format='wav')
    print(audiofile_wave)
    a=audiofile_wave
    
    def low_pass_filter(signal, sample_rate, cutoff_frequency):
        num_taps = int(sample_rate / (2 * cutoff_frequency))
        if num_taps % 2 == 0:
            num_taps += 1

 
        taps = np.ones(num_taps)
        taps /= num_taps

    # Use the filter function to apply the low-pass filter to the signal
        return np.convolve(signal, taps, mode='same')

    if uploaded_file is not None:
        # Open the WAV file
        wave_file = wave.open(audiofile_wave, 'r')

# Read the WAV file data
        sample_rate = wave_file.getframerate()
        num_samples = wave_file.getnframes()
        sample_width = wave_file.getsampwidth()
        signal = wave_file.readframes(num_samples)
        signal = np.frombuffer(signal, dtype=np.int16)

# Close the WAV file
        wave_file.close()

# Remove the noise using a low-pass filter
        filtered_signal = low_pass_filter(signal, sample_rate, cutoff_frequency=1000)

# Save the filtered signal to a new WAV file
        filtered_wave_file = wave.open('filtered.wav', 'w')
        filtered_wave_file.setnchannels(2)
        filtered_wave_file.setsampwidth(sample_width)
        filtered_wave_file.setframerate(sample_rate)
        filtered_wave_file.writeframes(filtered_signal.astype(np.int16))
        filtered_wave_file.close()
    
    
        wave_file = wave.open(audiofile_wave, 'r')
        sample_rate = wave_file.getframerate()
        num_samples = wave_file.getnframes()
        sample_width = wave_file.getsampwidth()
        signal = wave_file.readframes(num_samples)
        signal = np.frombuffer(signal, dtype=np.int16)
        wave_file.close()
    
        filtered_signal = low_pass_filter(signal, sample_rate, cutoff_frequency=100)
        filtered_wave_file = wave.open('filtered.wav', 'w')
        filtered_wave_file.setnchannels(2)
        filtered_wave_file.setsampwidth(sample_width)
        filtered_wave_file.setframerate(sample_rate)
        filtered_wave_file.writeframes(filtered_signal.astype(np.int16))
        filtered_wave_file.close()

with col2:
    st.header("Convert")
    if st.button('Convert 🔄'):
        if uploaded_file is not None:
            import speech_recognition as sr
            import json
            filename = "220714_2111.wav"
            # initialize the recognizer
            r = sr.Recognizer()
            # open the file
            with sr.AudioFile(filename) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)
        else:
            st.warning('Please Upload a file to convert', icon="⚠️")
    else:
        pass

with col3:
    st.header("Download file")
    text_contents = text
    st.download_button('Download 📥', text_contents)