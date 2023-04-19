import random
import streamlit as st
from PIL import Image
from playsound import playsound

def guess_number():
    st.title("Guess the Number")
    number = random.randint(1, 10)
    guess = st.number_input("Guess a number between 1 and 10:", min_value=1, max_value=10)
    if guess is not None:
        if guess == number:
            st.success("🎉🎂🎈 Happy Birthday! 🎈🎂🎉 May all your dreams come true and may this year bring you lots of joy, happiness and success. Enjoy your special day! 🎁🥳")
            balloons_img = Image.open("balloons.jpg")
            st.image(balloons_img, caption="Balloons!", use_column_width=True)
            st.write("Check out my personalized website at http://www.mywebsite.com")
            playsound("birthday_song.mp3")
        else:
            st.warning("Wrong! Guess again.")

guess_number()
