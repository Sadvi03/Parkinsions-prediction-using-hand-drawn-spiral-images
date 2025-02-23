
# Parkinson's Disease Prediction Using Hand-Drawn Spiral Images  

This is a **Streamlit web application** that predicts **Parkinson’s disease** using hand-drawn spiral images. The model is based on a **Convolutional Neural Network (CNN)** trained on spiral images from healthy and Parkinson’s patients.  

---

## 📌 **Features**  
- Upload a **hand-drawn spiral image**.  
- The app processes the image and makes a **prediction** using a trained **CNN model**.  
- Displays whether the person is **Healthy** or has **Parkinson's Disease**.  

---


## 1️⃣ Install Dependencies

Make sure you have Python 3.7+ installed. Then run:

```bash
pip install -r requirements.txt
```

## 2️⃣ Run the App

```bash
streamlit run app.py
```

## 📂 Project Structure

```
parkinsons_prediction_app/
├── models/
│   └── cnn_model.h5        # Trained CNN model
├── app.py                  # Streamlit app code
├── requirements.txt        # Dependencies list
└── README.md               # Project documentation
```

## 📷 How to Use

1. Run the app using `streamlit run app.py`.
2. Upload a spiral drawing image (JPG/PNG).
3. The app will process the image and display the prediction result.

## 📌 Model Details

* The CNN model was trained on hand-drawn spiral images from Parkinson’s patients and healthy individuals.
* The architecture consists of four convolutional layers, max pooling, dropout, and dense layers.
* The model is saved as `cnn_model.h5` and used for real-time predictions in the app.

## 🤖 Future Improvements

* Improve model accuracy with a larger dataset.
* Add explainability (e.g., Grad-CAM visualization).
* Deploy the app using Streamlit Cloud or AWS/GCP.

## 📜 License

This project is open-source under the MIT License.

## 📞 Contact

For any queries, feel free to reach out:

📧 Email: your_email@example.com
🔗 GitHub: yourusername
```
