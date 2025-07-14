import streamlit as st  #to run use streamlit run streamlit_app.py and venv\Scripts\activate

#page setup

about_page=st.Page(        
  page="views/about_me.py",
  title="About Me",
  icon="👤",
  default=True, #This is the default page when the app loads
)
page1=st.Page(
  page="views/sales.py",
  title="Sales Dashboard",
  icon="📊",
)
page2=st.Page(
  page="views/chatbot.py",
  title="Chatbot",
  icon="🤖",
)

#navigation bar witiuhout sections
# pg=st.navigation(pages=[about_page, page1, page2],)
# pg.run()

#navigation bar with sections

pg=st.navigation(
  {
    "Info": [about_page],
    "Projects": [page1,page2],
  }
)
st.sidebar.text("Made by Sujal")
pg.run()