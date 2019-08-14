def final_model(dic):
    from keras.models import load_model
    import numpy as np
    import os
    import pandas as pd
    
    df = pd.DataFrame(dic,index=[0])
    X_test = df.iloc[:,:].values
    current_path = os.getcwd()
    model_path = os.path.join(current_path, 'models')
    model = load_model(str(os.path.join(model_path, 'ANNmodel_5.h5py')))
    Y_pred = model.predict(X_test)
   
    results_dict={"Action":[],"Drama":[],"Horror":[],"Romance":[]}
    results_dict["Action"].append(float(Y_pred[0][0]*100))
    results_dict["Drama"].append(float(Y_pred[0][1]*100))
    results_dict["Horror"].append(float(Y_pred[0][2]*100))
    results_dict["Romance"].append(float(Y_pred[0][3]*100))

    return results_dict