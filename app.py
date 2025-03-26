import streamlit as st
import re
import random

# Strong password characters
SPECIAL_CHARACTERS = "!@#$%^&*"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(rf"[{re.escape(SPECIAL_CHARACTERS)}]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below:", feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    if length < 8:
        length = 8  # Ensure minimum length

    all_chars = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS + SPECIAL_CHARACTERS
    password = random.choice(LOWERCASE_LETTERS) + random.choice(UPPERCASE_LETTERS)
    password += random.choice(DIGITS) + random.choice(SPECIAL_CHARACTERS)
    password += ''.join(random.choices(all_chars, k=length - 4))
    
    return ''.join(random.sample(password, len(password)))  # Shuffle password

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input Field
password = st.text_input("Enter your password:", type="password")

# Check password strength
if password:
    result, suggestions = check_password_strength(password)
    st.markdown(f"**{result}**")

    if suggestions:
        st.warning("🔹 Suggestions to improve:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

# Password Generator
st.subheader("🔑 Generate a Strong Password")
length = st.slider("Select password length:", min_value=8, max_value=20, value=12)
if st.button("Generate Password"):
    strong_password = generate_strong_password(length)
    st.success(f"**Your Strong Password:** `{strong_password}` (Copy & Use)")

st.markdown("💡 **Tip:** Use a mix of uppercase, lowercase, numbers, and special characters for a strong password.")
