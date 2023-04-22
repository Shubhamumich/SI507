import streamlit as st
import subprocess
import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import time
import json
import os
from PIL import Image

def main():
    json_file = "Tokyotrial.json"
    with open(json_file, "r") as file:
        winner_data = json.load(file)

    json_file = "Riotrial.json"
    with open(json_file, "r") as file:
        winner_data2 = json.load(file)
    
    cmd = "ls -l"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    st.write(result.stdout.decode('utf-8'))
    activities = ["Home", "Tokyo Olympics", "Rio Olympics", "Plot Tree"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    st.sidebar.markdown("""Developed by:""")
    st.sidebar.markdown(""" 1. Shubham D. Deshpande  yogirana@umich.edu""")
    st.sidebar.markdown(""" Guide: QWERT ASDFF""")

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
        
        st.header("TREE")
        st.write("")

        class TreeNode:
            def __init__(self,data):
                self.data = data
                self.children = []
                self. parent = None

            def add_child(self,child):
                self.child = child 
                child.parent = self
                self.children.append(child)

            def get_level(self):
                level = 0 
                p = self.parent
                while p :
                    p = p.parent
                    level += 1
                return level 

            def get_tree_structure(self):
                tree_structure = ''
                prefix = '  ' * self.get_level() + '|--'
                tree_structure += prefix + self.data + '\n'
                if self.children:
                    for each in self.children:
                        tree_structure += each.get_tree_structure()
                return tree_structure

        def run():
            Tokyo_categories = list(set([dict['category'] for dict in winner_data]))
            Rio_categories = list(set([dict['category'] for dict in winner_data2]))
            root = TreeNode('Olympics')


            Tokyo = TreeNode('Tokyo')
            root.add_child(Tokyo)

            for category in Tokyo_categories:
                Tokyo_cat =TreeNode(category)
                Tokyo.add_child(Tokyo_cat)
                winner_name = [dict['name'] for dict in winner_data if category == dict['category']]
                Winner_country = [dict['country'] for dict in winner_data if category == dict['category']]
                winner_medal = [dict['medal'] for dict in winner_data if category == dict['category']]
                for i in range(len(winner_name)):
                    Tokyo_name = TreeNode(winner_name[i])
                    Tokyo_cat.add_child(Tokyo_name)
                    Tokyo_country = TreeNode(Winner_country[i])
                    Tokyo_name.add_child(Tokyo_country)
                    Tokyo_medal = TreeNode(winner_medal[i])
                    Tokyo_name.add_child(Tokyo_medal)
            
               

            Rio = TreeNode('Rio')
            root.add_child(Rio)

            for category in Rio_categories:
                Rio_cat = TreeNode(category)
                Rio.add_child(Rio_cat)
                winner_name = [dict['name'] for dict in winner_data2 if category == dict['category']]
                Winner_country = [dict['country'] for dict in winner_data2 if category == dict['category']]
                winner_medal = [dict['medal'] for dict in winner_data2 if category == dict['category']]
                for i in range(len(winner_name)):
                    Rio_name = TreeNode(winner_name[i])
                    Rio_cat.add_child(Rio_name)
                    Rio_country = TreeNode(Winner_country[i])
                    Rio_name.add_child(Rio_country)
                    Rio_medal = TreeNode(winner_medal[i])
                    Rio_name.add_child(Rio_medal)

            tree_structure = root.get_tree_structure()
            st.text(tree_structure)
        run()

if __name__ == "__main__":
    main()