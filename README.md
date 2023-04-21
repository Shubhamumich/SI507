# SI507- FINAL PROJECT
*******************************************************************************************************************************************************


The project is about extracting the data of competitive swimming sports results from 2 different event webpages using web scraping.The data that is not dynamic is stored in and accessed from the cache.The extracted data is stored in a CSV file. A Python file converts this CSV file into a tree and stores it in a JSON file. The streamlit based application provides an interactive and user-friendly interface where users can select options based on their requirements and get the results. The results are generated with the help of graph-based algorithms depending on the factors such as event name, category, participant name, etc. 


## Features

* Extracting data from 2 deifferent web pages
* Data stored in and accessed from cache
* Interactive web page
* Input from the user to get the prefered data
* Input from the user to get the prefered data
* Display details of each participant such as name,country, medal, etc based on graph

## Getting Started

### Prerequisites
* Python 3.x


#### Packages
- Streamlit
- requests 
- BeautifulSoup
- Plotly
- pandas
- numpy

#### Running the Program
Open a terminal in the project directory and run the following command:

      streamlit run stream.py
      
      Click any url to view web app.
      Local URL: http://localhost:8501
      Network URL: http://192.168.10.38:8501
      
#### Interacting with the Program
1. Select the Option from the side-bar select box
2. from the drowp-down menu choose the required option
3. Click on categories or winners to get the related data

## Data structure

A tree is a data structure that represents a hierarchical structure consisting of nodes connected by edges. This data structure provides a simple, intuitive way to organize and navigate hierarchical data. The topmost node in a tree is called the root node, which will be the sports name, and each node in the tree can have any number of child nodes consisting of various events name and each child node have its child node of it's own whic consists of the name of the winners and so on. The child nodes of the winner nodes will contain the information related to the participant such as his country name. The options for selection are generated using a graph-based algorithm which provides the required results.






*********************************************************************************************************************************


