import streamlit as st
import re
import secrets
import string

import streamlit as st
import re
import secrets
import string

def check_strength(password):
    strength = 0
    suggestions = []
    
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password in common_passwords:
        return 0, ["This password is too common. Choose a more unique one."]
    
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
    
    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")
    
    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    else:
        suggestions.append("Use at least one special character (@, $, !, %, *, ?, &, #).")
    
    return strength, suggestions

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        strength, suggestions = check_strength(password)
        
        strength_labels = ["Very Weak 🔴", "Weak 🟠", "Medium 🟡", "Strong 🟢", "Very Strong ✅"]
        strength_color = ["red", "orange", "yellow", "blue", "green"]
        
        st.write(f"### Strength: {strength_labels[min(strength, 4)]}", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{strength_color[min(strength, 4)]}; font-size:20px;'><b>{strength_labels[min(strength, 4)]}</b></p>", unsafe_allow_html=True)
        
        st.progress(min(max(strength / 4, 0), 1))
        
        if suggestions:
            st.warning("Improve your password:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.success("Your password is very strong! ✅")
            st.balloons()
        
        st.write("### 🔑 Need a Strong Password?")
        if "new_password" not in st.session_state:
            st.session_state["new_password"] = generate_password()
        
        st.code(st.session_state["new_password"], language='plaintext')
        
        if st.button("Generate New Password"):
            st.session_state["new_password"] = generate_password()
            st.rerun()

if __name__ == "__main__":
    main()
