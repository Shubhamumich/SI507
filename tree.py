import streamlit as st
import json

json_file = "./Data/Tokyo_data.json"
with open(json_file, "r") as file:
    winner_data = json.load(file)

json_file = "./Data/Rio_data.json"
with open(json_file, "r") as file:
    winner_data2 = json.load(file)

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
        with open("./tree.json", "w") as outfile:
                json.dump(tree_structure, outfile, indent=4)
        return tree_structure

def run():

    Tokyo_categories = list(set([dict['category'] for dict in winner_data]))
    Rio_categories = list(set([dict['category'] for dict in winner_data2]))

    st.header("TREE")
    st.write("")

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