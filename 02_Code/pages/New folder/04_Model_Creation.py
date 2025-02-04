import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    st.title("🤖 Model Creation")

    if "uploaded_file" in st.session_state:
        df = pd.read_csv(st.session_state["uploaded_file"])
        
        target = st.selectbox("Select Target Column", df.columns)
        
        if st.button("Train Model"):
            X = df.drop(columns=[target])
            y = df[target]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            st.success(f"Model trained successfully! Accuracy: {acc:.2f}")
    else:
        st.warning("Please upload a CSV file from the sidebar.")

if __name__ == "__main__":
    main()
