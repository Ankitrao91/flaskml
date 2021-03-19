import json
import numpy as np
from flask_cors import CORS
# import joblib
import pickle
# from keras.models import load_model
# OR
# from tensorflow.keras.models import load_model
# 
from flask import Flask, request
# 
# import helper

app = Flask(__name__)
CORS(app)

# model_path = "random_forest_regression_model.h5"

@app.route('/<sellingPrice>', methods=['GET'])
def index_page(sellingPrice):
    model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
    Kms_Driven2=np.log(27000)
    print(Kms_Driven2)
    Sp = sellingPrice
    print(Sp)
    prediction=model.predict([[Sp,Kms_Driven2,0,5,1,0,1,0]])
    
    output=round(prediction[0],2)
    
    string=str(output)
    return_data = {
        "error" : "0",
        "message" : "prediction",
        "result" : string
        

    }
    return string
    # return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')
    # return output
# @flask_app.route('/classify', methods=['POST'])
# def classify_malaria_cells():
#     try:
#         if "malaria_cell_image" in request.files and request.files['malaria_cell_image'] is not None:
#             malaria_image = request.files['malaria_cell_image']
#             is_successful, preprocessed_image = helper.preprocess_img(malaria_image)
#             if is_successful:
#                 # load malaria model
#                 malaria_model = load_model(model_path)
#                 #
#                 score = malaria_model.predict(preprocessed_image)
#                 label_indx = np.argmax(score)
#                 classification = "Normal" if label_indx == 0 else "Infected"
#                 max_score = round(np.max(score), 2)
#                 return_data = {
#                     "error" : "0",
#                     "message" : "Successful",
#                     "classification" : classification
#                 }
#             else:
#                 return_data = {
#                     "error" : "1",
#                     "message" : "Image preprocessing error"
#                 }
#         else:
#             return_data = {
#                 "error" : "1",
#                 "message" : "Invalid parameters"
#             }
#     except Exception as e:
#         return_data = {
#             "error" : "1",
#             "message" : f"[Error] : {e}"
#         }
#     return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')

if __name__ == "__main__":
    app.run(port=8080, debug=True, threaded=False)