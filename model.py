import streamlit as st


from PIL import Image



#opening the image


def show():
    st.header("Models and their Accuracies")
    image = Image.open('C:\\Users\\Dell\\Desktop\\majorproject\\model_tables.png')
    col1,col2,col3,col4=st.columns(4)
    with col2:
        st.image(image,width=350,output_format="auto")
    image= Image.open('C:\\Users\\Dell\\Desktop\\majorproject\\accuracy.png')
    st.write("Table displaying accuracy scores (%) of machine learning models used in the water quality monitoring system.")
    col1,col2,col3,col4,col5=st.columns(5)
    with col2:
        st.image(image, caption=None,output_format="auto",width=500)
    st.write("The image displays a bar graph representing the accuracy (%) of various machine learning models employed in the water quality monitoring system. The x-axis denotes the different algorithms, such as Decision Tree, Random Forest, KNN, SVM, AdaBoost, and XGBoost. Meanwhile, the y-axis represents accuracy in percentage. Higher bars indicate higher accuracy levels. XGBoost emerges as the most accurate algorithm, boasting an accuracy of approximately 99.328859%")
    st.header("Conclusion")
    st.write("In this project, XGBoost, known for its high accuracy percentage, has been employed as the primary algorithm for determining water quality. Leveraging its superior predictive capabilities, XGBoost analyzes various water quality parameters and provides accurate assessments in real-time. This ensures that the water quality monitoring system delivers reliable and timely information to authorities, enabling prompt action to maintain water safety and mitigate risks.")
     
   