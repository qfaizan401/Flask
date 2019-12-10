from flask import Flask, jsonify, request, render_template
import numpy as np
from PIL import Image
from keras.models import load_model
import tensorflow as tf
graph = tf.get_default_graph()

app = Flask(__name__)

model = load_model('swift_and_wagonR_final.h5')

@app.route("/")
def forms():
    return render_template("model.html")


@app.route('/image', methods=['POST'])
def index():
    data = request.files['file']
    # keras.backend.resize_images(data,
    #                             150,150,
    #                             data_format = 'channels_first',
    #                             interpolation='nearest')
    img = Image.open(data)
    img = np.asarray(img)
    #img = np.resize(img,(150,150))
    img = img.reshape(1,150,150,3)
    img = img/255
    with graph.as_default():
        prediction = model.predict(img)
        if prediction < .5:
            return jsonify({"success": True, "name": 'swift'})
        else:
            return jsonify({"success": True, "name": "wagonR"})


if __name__ == "__main__":
    app.run(debug = True)




# from flask import Flask,jsonify,request,render_template
# from keras.models import load_model
# from PIL import Image
# from keras.preprocessing import image
# import tensorflow as tf
#
# gragh = tf.get_default_graph()
#
# app = Flask(__name__)
# modeldata = load_model("cats_and_dogs_small_1.h5")
#
# @app.route('/')
# def model ():
#     return render_template('model.html')
#
# @app.route('/home',methods=["POST"])
# def index ():
#     data = request.files['file']
#     #img = image.load_img(data,target_size=(150, 150))
#     img = Image.open(data)
#     img = image.img_to_array(img)
#     img = img.reshape((1,)+img.shape)
#     img = img/255
#     with graph.as_default():
#         prediction = modeldata.predict(img)
#         if prediction < .5:
#             return jsonify({'success':True,
#                             'name':'cat'})
#         else:
#             return jsonify({'sucess':True,
#                             'name':'dog'})
#     return jsonify({'success':False})
#
# if __name__ == '__main__':
#     app.run(debug=True)