def call(movie_path):
    import os
    import video_extractor
    import delete_images
    import CNNworking
    import final_working
    import audio_testing
    import rgb
    current_path = os.getcwd()
    movie_extraction_path = os.path.join(current_path, 'movie_extraction')
    final_dict={}
    if os.path.exists(os.path.join(os.getcwd(), 'movie_extraction')) == False:
        os.makedirs(os.path.join(os.getcwd(), 'movie_extraction'))
    else:
        pass
    try:
        video_extractor.extractframes(movie_extraction_path, str(movie_path))
        try:
            CNN_dic = CNNworking.model()
            CNN_dic2=final_working.final_model(CNN_dic)
            final_dict.update(CNN_dic2)
        except:
            CNN_dic2={"Action":[0],"Drama":[0],"Horror":[0],"Romance":[0]}
            final_dict.update(CNN_dic2)
        try:
            rgb_dic=dict(rgb.main())
            final_dict.update(rgb_dic)

        except:
            rgb_dic={"Action_rgb":[0],"Romance_rgb":[0],"Drama_rgb":[0],"Horror_rgb":[0]}
            final_dict.update(rgb_dic)
    except:
            CNN_dic2={"Action":[0],"Drama":[0],"Horror":[0],"Romance":[0]}
            final_dict.update(CNN_dic2)
            rgb_dic={"Action_rgb":[0],"Romance_rgb":[0],"Drama_rgb":[0],"Horror_rgb":[0]}
            final_dict.update(rgb_dic)
    try:
        audio_dic = dict(audio_testing.predict_genre(str(movie_path)))
        final_dict.update(audio_dic)
    except:
        audio_dic={"Action_audio":[0],"Romance_audio":[0],"Drama_audio":[0],"Horror_audio":[0]}
        final_dict.update(audio_dic)        
    
    delete_images.empty_folder(movie_extraction_path)
    return final_dict
        




