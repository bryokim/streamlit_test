import streamlit as st
import pymongo
import urllib.parse


url = f"mongodb+srv://{urllib.parse.quote_plus(st.secrets['username'])}:{urllib.parse.quote_plus(st.secrets['password'])}@cluster0.atxx7vd.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(url)


client = init_connection()


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.swam
    items = db.users.find()
    items = list(items)  # make hashable for st.cache_data
    return items


items = get_data()

# Print results.
for item in items:
    st.write(f":blue[{item['username']}]")
