import streamlit as st

st.header('Display and image with st.image')
st.image('image.jpg', caption='Beautiful City', width=500)

st.header('Display a video')
video_file = open('waterfalls.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.header('Display an audio file')
audio_file = open('audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
