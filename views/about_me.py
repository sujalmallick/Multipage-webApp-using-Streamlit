import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me") # This creates a dialog box for the contact form.popup effect
def contact_dialog():
    contact_form()  # Call the contact form function to display it in the dialog

col1,col2=st.columns(2,gap="small",vertical_alignment="center")   #This line creates two columns side by side in your Streamlit app layout.

with col1: #Anything inside with col1: will appear in the left column.
  st.image("./assets/profile-pic.png",width=200)
with col2:
  st.title("Sujal Mallick",anchor=False)
  st.write("I am CS Engineer with a passion for AI and Machine Learning. I love to explore new technologies and apply them to solve real-world problems.") #with col2: places content in the right column.

# st.title(...) displays a large heading — your name.

# anchor=False disables the little "link" icon that usually appears next to titles (for clean design).

# st.write(...) adds a short paragraph describing who you are — a mini bio.

st.markdown("###")  # Adds vertical space padding between sections

if st.button("Contact Me"):
  contact_dialog()
 
st.write("\n")
st.subheader("Experience and Qualifications",anchor=False)

st.write("""
### 🎓 Education
**B.Tech in Computer Science Engineering**  
Thapar University  
*Expected Graduation: 2027*

### 💻 Technical Skills
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Node.js, Express.js  
- **Web Frameworks:** Streamlit  
- **Databases:** MongoDB (learning)  
- **Version Control:** Git, GitHub  
- **APIs & Tools:** OpenAI API,Webhooks, YouTube Data API  


### 🎨 Creative Skills
- Skilled in **photography**, **videography**, and **editing**
""")
