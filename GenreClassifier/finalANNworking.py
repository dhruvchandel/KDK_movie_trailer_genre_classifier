def final_model(dic):
    from keras.models import load_model
    import numpy as np
    import os
    import pandas as pd
    
    df = pd.DataFrame(dic,index=[0])
    X_test = df.iloc[:,1:].values
    current_path = os.getcwd()
    model_path = os.path.join(current_path, 'models')
    model = load_model(str(os.path.join(model_path, 'finalANNmodel_4.h5')))
    Y_pred = model.predict(X_test)
    
    pred = np.array([Y_pred[0][0],Y_pred[0][1],Y_pred[0][2],Y_pred[0][3]])
    max_index=np.argmax(pred)

    print('action   --->%.2f'%(float(Y_pred[0][0])*100),'percent',sep = ' ')
    print('drama    --->%.2f'%(float(Y_pred[0][1])*100),'percent',sep = ' ')
    print('horror   --->%.2f'%(float(Y_pred[0][2])*100),'percent',sep = ' ')
    print('romance  --->%.2f'%(float(Y_pred[0][3])*100),'percent',sep = ' ')


    label_dic = {
        0:'action',
        1:'drama',
        2:'horror',
        3:'romance',
    }
    
    return {"Name":dic["Name"], "Genre":label_dic[max_index]}