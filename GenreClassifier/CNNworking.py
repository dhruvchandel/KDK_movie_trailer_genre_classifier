''' implementing the model we made'''
def model():
    import os
    import numpy as np
    from keras.models import load_model
    from keras.preprocessing import image
    from pathlib import Path
    
    def get_images(p):
        images = []
        for img_dir in p.glob('*'):
            img = image.load_img(img_dir, target_size = (100,100))
            img_array = image.img_to_array(img, dtype = 'float32')/255
            images.append(img_array)
        
        return images
    
    
    def percentage_maker(Y_pred):
        Y_new = []
        for i in range(Y_pred.shape[0]):
            yarr = max(Y_pred[i])
            for j in range(Y_pred.shape[1]):
                if Y_pred[i][j] == yarr:
                    Y_new.append(j)
                    break
    
        percentage = np.zeros(Y_pred.shape[1])
        for j in range(len(Y_new)):
            percentage[Y_new[j]] += 1/len(Y_new)
        
        return percentage
    
    label_dic = {'action': 0, 
                 'cars': 1, 
                 'drama': 2, 
                 'explosion': 3, 
                 'horror': 4, 
                 'party': 5, 
                 'robot': 6, 
                 'romance': 7}
    #os.chdir('D:/project_x/image_classifier')
    current_path = os.getcwd()
    frames_path = os.path.join(current_path, 'movie_extraction')
    model_path = os.path.join(current_path, 'models')
    X_test =get_images(Path(frames_path))
    X_test = np.array(X_test)
    model = load_model(os.path.join(model_path, 'CNNmodel_5.h5py'))
    Y_pred = model.predict(X_test)
    
    Y_percentage = percentage_maker(Y_pred)
    final_dic = label_dic.copy()
    for key, value in final_dic.items():
        final_dic[key] = float('%0.2f'%(Y_percentage[value]*100))

    
    return final_dic
    
    