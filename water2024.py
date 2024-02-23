import streamlit as st
import pandas as pd
import pickle
import os

# Load the data
model_path ="C:/Users/mmnm2/Desktop/PROJECT 45 END/RandomForestClassifier_model1.sav"
data_path = r"C:\Users\mmnm2\Desktop\PROJECT 45 END\water.csv"
df = pd.read_csv(data_path)

# Load the trained model
def load_model():
    try:
        if os.path.exists(model_path):
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            print("Model loaded successfully!")
            return model
        else:
            print(f"Model file not found at: {model_path}")
            return None
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')
    
    model = load_model()

    st.sidebar.write("")
    st.sidebar.header("Feature Selection")

    ph = st.text_input("ph")
    Hardness = st.text_input("Hardness")
    Solids = st.text_input("Solids")
    Chloramines = st.text_input("Chloramines")
    Sulfate = st.text_input("Sulfate")
    Conductivity = st.text_input("Conductivity")
    Organic_carbon = st.text_input("Organic_carbon")
    Trihalomethanes = st.text_input("Trihalomethanes")
    Turbidity = st.text_input("Turbidity")



    # Check if the inputs are valid before predicting
    if input_df.isnull().values.any():
        st.write('Please fill in all the fields.')
    else:
        # Create a button to execute the prediction
        if st.button('Predict Potability'):
            if model is not None:
                prediction = model.predict(input_df)
                if prediction[0] == 0:
                    st.write('The water is not potable.')
                else:
                    st.write('The water is potable.')

if __name__ == "__main__":
    main()
