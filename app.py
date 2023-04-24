import streamlit as st
import subprocess
import json
from PIL import Image
import tree

def main():
    json_file = "./Data/Tokyo_data.json"
    with open(json_file, "r") as file:
        winner_data = json.load(file)

    json_file = "./Data/Rio_data.json"
    with open(json_file, "r") as file:
        winner_data2 = json.load(file)
    
    cmd = "ls -l"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    st.write(result.stdout.decode('utf-8'))
    activities = ["Home", "Tokyo Olympics", "Rio Olympics", "Plot Tree"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    st.sidebar.markdown("""Developed by:""")
    st.sidebar.markdown(""" 1. Shubham D. Deshpande  yogirana@umich.edu""")

    if choice == "Home":
        st.title("Swimming Championship")
        img = Image.open("olympics.jpg")
        st.image(img, width=700)
        st.subheader("About this app:")
        html_temp_about1= """<div style="background-image: url('img_girl.jpg');"">
                                    <h4 style="color:white;text-align:center;"><center>
                                    The project is about extracting the data of competetive swimming sports results from 2 different event websites, comparing the data, visualising it in various graphical forms, and displaying 
                                    the data in the interactive dashboard using streamlit framework</center></h4>
                                    </div>
                                    </br>"""
        st.markdown(html_temp_about1, unsafe_allow_html=True)
        html_temp4 = """
                             		<div style="background-image: url('img1.png');">
                                 
                             		<h4 style="color:white;text-align:center;">In this application users will be able to interact and choose between the provided options for selecting and displaying data. </h4>
                             		<h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                             		</div>
                             		<br></br>
                             		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

    elif choice == "Tokyo Olympics":

        options = ["Select your choice", "All_categories"]
        selected_option = st.selectbox("Select an option", options)
        
        if selected_option == "All_categories":
            html_temp_home1 = """<div style="background-color:#1152F7;padding:10px">
                                        <h4 style="color:white;text-align:center;">
                                        Categories</h4>
                                        </div>
                                        </br>"""
            st.markdown(html_temp_home1, unsafe_allow_html=True)
            st.write("""
                These are the categories included in Tokyo olympics:
                """)
            cat = ["Select your category"]
            cat = cat + list(set([dict['category'] for dict in winner_data]))
            

            choice = st.selectbox("Select Category", cat)
            if choice != "Select your category":
                html_temp_home1 = """<div style="background-color:#1152F7;padding:10px">
                                        <h4 style="color:white;text-align:center;">
                                        Results</h4>
                                        </div>
                                        </br>"""
                st.markdown(html_temp_home1, unsafe_allow_html=True)
                st.write("""
                    These are the reults for the corresponding category:
                    """)
                winner_name = [dict['name'] for dict in winner_data if choice == dict['category']]
                Winner_country = [dict['country'] for dict in winner_data if choice == dict['category']]
                winner_medal = [dict['medal'] for dict in winner_data if choice == dict['category']]
                col =[]
                for i in range(len(winner_name)):
                    if winner_medal[i] == 'Gold':
                        col.append('#ffd700')
                    elif winner_medal[i] == 'Silver':
                        col.append('#c0c0c0')
                    else:
                        col.append('#CD7F32')

                    html_temp_home2 = f"""<div style="background-color:{col[i]};padding:10px">
                                        <h5 style="color:black;text-align:center;">
                                        {winner_name[i]}</h5>
                                        <h5 style="color:black;text-align:center;">
                                        {Winner_country[i]}</h5>
                                        <h5 style="color:black;text-align:center;">
                                        {winner_medal[i]}</h5>
                                        </div>
                                        </br>"""
                    st.markdown(html_temp_home2, unsafe_allow_html=True)   

    elif choice == "Rio Olympics":
        options = ["Select your choice", "All_categories"]
        selected_option = st.selectbox("Select an option", options)
        
        

        if selected_option == "All_categories":
            html_temp_home1 = """<div style="background-color:#1152F7;padding:10px">
                                        <h4 style="color:white;text-align:center;">
                                        Categories</h4>
                                        </div>
                                        </br>"""
            st.markdown(html_temp_home1, unsafe_allow_html=True)
            st.write("""
                These are the categories included in Tokyo olympics:
                """)
            cat = ["Select your category"]
            cat = cat + list(set([dict['category'] for dict in winner_data2]))
            

            choice = st.selectbox("Select Category", cat)
            if choice != "Select your category":
                html_temp_home1 = """<div style="background-color:#1152F7;padding:10px">
                                        <h4 style="color:white;text-align:center;">
                                        Results</h4>
                                        </div>
                                        </br>"""
                st.markdown(html_temp_home1, unsafe_allow_html=True)
                st.write("""
                    These are the reults for the corresponding category:
                    """)
                winner_name = [dict['name'] for dict in winner_data2 if choice == dict['category']]
                Winner_country = [dict['country'] for dict in winner_data2 if choice == dict['category']]
                winner_medal = [dict['medal'] for dict in winner_data2 if choice == dict['category']]
                col =[]
                for i in range(len(winner_name)):
                    if winner_medal[i] == 'Gold':
                        col.append('#ffd700')
                    elif winner_medal[i] == 'Silver':
                        col.append('#c0c0c0')
                    else:
                        col.append('#CD7F32')

                    html_temp_home2 = f"""<div style="background-color:{col[i]};padding:10px">
                                        <h5 style="color:black;text-align:center;">
                                        {winner_name[i]}</h5>
                                        <h5 style="color:black;text-align:center;">
                                        {Winner_country[i]}</h5>
                                        <h5 style="color:black;text-align:center;">
                                        {winner_medal[i]}</h5>
                                        </div>
                                        </br>"""
                    st.markdown(html_temp_home2, unsafe_allow_html=True)

    elif choice == "Plot Tree":
        tree.run()
        
        

if __name__ == "__main__":
    main()