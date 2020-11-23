import pandas as pd
import numpy as np
import streamlit as st
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
count=0


    


def scatter(df):
    plt.figure(figsize=(18,6))
    plt.title("Scatter Plot between HeartRate and BreathRate")
    sns.scatterplot(df["HeartRate"],df["BreathRate"])
    return st.pyplot()



def linechart(df):   
    X = np.array(df["group"])
    plt.figure(figsize=(18, 6))
    plt.title("Line Chart betwen HeartRate and time(seconds)")
    z = np.polyfit(X, df["HeartRate"], 2)
    p = np.poly1d(z)
    plt.plot(X,p(X),"r--")
    plt.plot(X, df["HeartRate"])
    st.pyplot()
    
               
    X = np.array(df["group"])
    plt.figure(figsize=(18, 6))
    plt.title("Line Chart betwen BreathRate and time(seconds)")
    z = np.polyfit(X, df["BreathRate"], 2)
    p = np.poly1d(z)
    plt.plot(X,p(X),"r--")
    plt.plot(X, df["BreathRate"])
    st.pyplot()
    

def dbchart(df):
    st.text("Density and boxplot of HeartRate and BreathRate")
    fig, axs = plt.subplots(2,2,figsize=(15,15))
    sns.distplot(df["HeartRate"],ax=axs[0,0])
    sns.boxplot(df["HeartRate"],ax=axs[0,1])
    sns.distplot(df["BreathRate"],ax=axs[1,0])
    sns.boxplot(df["BreathRate"],ax=axs[1,1])
    return st.pyplot()



def split_dataframe(df, chunk_size = 120): 
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks
    
    


def windows1(windows):
    for i in range(0,len(windows)):
        title1 = "Window " +str(i)
        st.text(title1)
        x = "Density , boxplot and lineplot of HeartRate and BreathRate of Window{}".format(i)
        st.text(x)
        fig,axs = plt.subplots(1,4,figsize=(15,5))
        plt.figure(figsize=(10,10))
        sns.kdeplot(windows[i]["HeartRate"],ax=axs[0])  
        sns.boxplot(windows[i]["HeartRate"],ax=axs[1])
        sns.kdeplot(windows[i]["BreathRate"],ax=axs[2])  
        sns.boxplot(windows[i]["BreathRate"],ax=axs[3])
        st.pyplot(fig)
          
        q = "Line Chart betwen HeartRate and time(seconds) for window {}".format(i)
        plt.title(q)
               
        X = np.array(windows[i]["group"])
        plt.figure(figsize=(10, 3))
        z = np.polyfit(X, windows[i]["HeartRate"], 1)
        p = np.poly1d(z)
        plt.plot(X,p(X),"r--")
        plt.plot(X, windows[i]["HeartRate"])
        st.pyplot()            
        X = np.array(windows[i]["group"])
        plt.figure(figsize=(10, 3))
        z = np.polyfit(X, windows[i]["BreathRate"], 1)
        p = np.poly1d(z)
        plt.plot(X,p(X),"r--")
        plt.plot(X, windows[i]["BreathRate"])
        st.pyplot()
               
 



def call_all(df):
    def time_conversion(x):
        z = datetime.datetime.utcfromtimestamp(x)
        return z
    def group(x):
        global count
        count+=30
        return count
    df["group"] = df["TimeStamp"].apply(group)
    df["Time"]= df["TimeStamp"].apply(time_conversion)
    st.dataframe(df.head())
    scatter(df)
    linechart(df)
    dbchart(df)
    split_dataframe(df, chunk_size = 120)
    windows = split_dataframe(df, chunk_size=120)
    x = "There are total {} windows in csv{}".format(len(windows),1)
    st.text(x)
    windows1(windows)
st.header("Select Csv Number")
option = st.selectbox("",('1', '2', '3','4','5','6','7','8','9','10'))

if option =='1':

    z = ("csv_1.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='2':

    z = ("csv_2.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='3':
    p=1
    z = ("csv_3.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='4':
    p=1
    z = ("csv_4.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='5':
    p=1
    z = ("csv_5.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='6':
    p=1
    z = ("csv_6.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='7':
    p=1
    z = ("csv_7.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='8':
    p=1
    z = ("csv_8.csv")
    df = pd.read_csv(z)
    call_all(df)
    
    

if option =='9':
    p=1
    z = ("csv_9.csv")
    df = pd.read_csv(z)
    call_all(df)

if option =='10':
    p=1
    z = ("csv_10.csv")
    df = pd.read_csv(z)
    call_all(df)
