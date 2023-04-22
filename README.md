# SI507- FINAL PROJECT
*******************************************************************************************************************************************************


The objective of this project is to implement a web scraping solution to extract data from two distinct web pages related to competitive swimming sports results. To optimize performance and reduce server requests, non-dynamic data is cached for faster retrieval. The extracted data is transformed into a tree structure using a Python script and stored in a JSON file format for easier access and manipulation. To provide a user-friendly interface, a Streamlit-based application is implemented, which enables users to filter and retrieve data based on various criteria.

![olympics](https://user-images.githubusercontent.com/131201063/233807759-66ceb3bc-6eb9-4201-bc0d-ec73e602f50d.jpg)


## Features

* Involves web scraping techniques to extract data from two distinct web pages
* Data stored in and accessed from cache
* Interactive web page
* Input from the user to get the prefered data
* Display details of each participant such as name,country, medal, etc.

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

      streamlit run app.py
      
      Click any url to view web app.
      Local URL: http://localhost:8501
      Network URL: http://192.168.10.38:8501
      
#### Interacting with the Program
1. Select the Option from the side-bar select box
2. From the drop-down menu choose the preffered category
3. Click on categories to view the results
4. Visualise the results tree by selecting the option

## Data structure

A tree is a highly efficient data structure used to represent hierarchical relationships between elements. In this project, a tree structure is used to represent the hierarchical relationship between different swimming events, categories and winners.The topmost node in the tree represents the sports name, and each subsequent node represents an event. Each event node can have multiple categories and each category has child nodes, representing the winners of that event category. The child nodes of each winner represents the country and the medal received. To enable users to navigate and select specific data, the application uses easy but effective interface to generate results based on the user's input criteria. This allows users to efficiently and accurately retrieve the data.







*********************************************************************************************************************************


