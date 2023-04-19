import streamlit as st
import subprocess
import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import time
import os
import plotly.graph_objs as go



def main():
    # Face Analysis Application #
    st.title("Swimming Championship")
    cmd = "ls -l"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    st.write(result.stdout.decode('utf-8'))
    #activities = ["Home", "Live Facial Emotion Detection", "Image Emotion Detection", "About"]
    activities = ["About", "Tokyo Olympics", "Plot Tree", "Fina swimmimg championship", "ABX"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
 
    st.sidebar.markdown("""Developed by:""")
    st.sidebar.markdown(""" 1. Shubham D. Deshpande  yogirana@umich.edu""")

    st.sidebar.markdown(""" Guide: QWERT ASDFF""")
    
    

    if choice == "About":
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

        html_temp_home1 = """<div style="background-color:#1152F7;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Categories</h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
        st.write("""
                 These are the categories included in Tokyo olympics:
                 """)

        url_to_call = "https://olympics.com/en/olympic-games/tokyo-2020/results/swimming"

# cache timeout in seconds
        cache_timeout = 60 * 60 * 24 # 1 day

# Check if the data is already cached
        cached_data = None
        try:
            with open('cached_data.html', 'r') as f:
                cached_data = f.read()
            print("Using cached data")
        except:
            print("No cached data found")

# If the data is not cached or the cache has expired, scrape the website
        if not cached_data or time.time() - os.path.getmtime('cached_data.html') > cache_timeout:
            print("Scraping website")
    # Make a GET request to the URL
            response = requests.get(url_to_call, headers={'User-Agent': "Mozilla/5.0"})
            print(response.status_code)    # o/p = 200. Response success
            response_code = response.status_code
            if  response_code != 200:
                print("Error Occured")
        
    # Parse the HTML content using Beautiful Soup
        html_content = response.content
    
        dom = BeautifulSoup(html_content, 'html.parser')

        all_categories = dom.select("div.hgxeXK")
        for each_category in all_categories:
            h_link = each_category.h2
            data_text = h_link.text
            print(data_text)
            st.write(data_text)
        
        st.markdown(
                """
                <style>
                .reportview-container {
        img = Image.open("img1.png")
                   
                }
            .sidebar .sidebar-content {
        img = Image.open("img1.png")
                    
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        
        

    elif choice == "Plot Tree":
        
        st.header("Tree")
        st.write("Click on start to use webcam and detect your face emotion")
        
        

       

# Define your tree structure
        class Node:
            def __init__(self, value, depth=0):
                self.value = value
                self.children = []
                self.depth = depth

# Create your tree
        root = Node(1)
        root.children.append(Node(2))
        root.children.append(Node(3))
        root.children[0].children.append(Node(4))
        root.children[0].children.append(Node(5))
        root.children[1].children.append(Node(6))

# Define a recursive function to traverse the tree and create Plotly traces
        def traverse(node):
            trace = go.Scatter(
                x=[node.value],
                y=[node.depth],
                text=str(node.value),
                mode='markers+text',
                marker=dict(size=20),
                hoverinfo='text'
            )
            for child in node.children:
                child_trace = traverse(child)
                trace = trace + child_trace
            return trace

# Create the Plotly figure
        fig = go.Figure(data=traverse(root))

# Set the layout
        fig.update_layout(
            title='General Tree Visualization',
            xaxis=dict(title='Value'),
            yaxis=dict(title='Depth'),
            hovermode='closest'
        )

# Display the figure on Streamlit
        st.plotly_chart(fig)

					

    elif choice == "About":
        st.subheader("About this app")
        html_temp_about1= """<div style="background-image: url('img_girl.jpg');"">
                                    <h4 style="color:white;text-align:center;">
                                    Real time face emotion detection application using OpenCV, CNN model and Streamlit.</h4>
                                    </div>
                                    </br>"""
        st.markdown(html_temp_about1, unsafe_allow_html=True)

        html_temp4 = """
                             		<div style="background-image: url('img1.png');">
                                 
                             		<h4 style="color:white;text-align:center;">This Application is developed by GROUP 1 using Streamlit Framework, Opencv, Tensorflow and Keras library for demonstration purpose. </h4>
                             		<h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                             		</div>
                             		<br></br>
                             		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

    # else:
    #     pass


if __name__ == "__main__":
    main()