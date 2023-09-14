
import time, json, os
import base64
from PIL import Image
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import base64 
import numpy as np
import logging
log = logging.getLogger('werkzeug')
# log.disabled = True


from mobileNetV3 import MobileNetV3
import torch
device = torch.device("cpu")
model = MobileNetV3(mode='large', classes_num=2, input_size=224, width_multiplier=1.0)
model.load_state_dict(torch.load(r".\media\data2\chenjiarong\saved-model\MobileNetV3\MobileNetV3-large-tableware-wm1.0-dp0.2-lr0.01-bs256-ed0.0-ls0.0-sgd6e-05-bn0.1-epochs100-seedNone-determinFalse-NoBiasDecayFalse-zeroGammaFalse-mixupFalse-cos5&0.0\epoch_98.pth"))
model.eval()


from torchvision import transforms

data_transforms = {'inference': transforms.Compose([
            transforms.Resize([224,224]),
            transforms.ToTensor(),
            transforms.Normalize([0.6771, 0.6447, 0.6065], [0.2182, 0.2205, 0.2335]),
        ])}

# read image
from PIL import Image
import glob
import io


app = Flask(__name__)
api = Api(app)


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        docname = posted_data['docname']
        imagestr = posted_data['imagestr']
        imgdata = base64.b64decode(imagestr)
        # print(imgdata)
        img = Image.open(io.BytesIO(imgdata))
        img = data_transforms['inference'](img)
        img = img.unsqueeze(0)
        # print(img.shape)

        try:
            # predict
            output = model(img)
            # print(output.argmax().item()) 
            if output.argmax().item() == 0:
                out_res=[docname, '0', 'No']
            else:
                out_res=[docname, '1', 'Yes']
        except:                
            out_res=[docname, '9999', 'unknow err']
        return jsonify({"texts": out_res})
api.add_resource(MakePrediction, '/predict')

if __name__ == '__main__': 

    app.run(debug=False, threaded=False, port=5000, host='0.0.0.0')  # , host='192.168.243.27' 


