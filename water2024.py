import streamlit as st

    data = {
        'ph': [float(ph) if ph else None],
        'Hardness': [float(Hardness) if Hardness else None],
        'Solids': [float(Solids) if Solids else None],
        'Chloramines': [float(Chloramines) if Chloramines else None],
        'Sulfate': [float(Sulfate) if Sulfate else None],
        'Conductivity': [float(Conductivity) if Conductivity else None],
        'Organic_carbon': [float(Organic_carbon) if Organic_carbon else None],
        'Trihalomethanes': [float(Trihalomethanes) if Trihalomethanes else None],
        'Turbidity': [float(Turbidity) if Turbidity else None]
    }
    input_df = pd.DataFrame(data)

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
