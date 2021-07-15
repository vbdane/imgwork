from cv2 import cv2, dnn_superres
import os

def upscale(img_path, model):
    model_dict = {"fsrcnn2": [r"models/FSRCNN_x2.pb", 2, "fsrcnn"],
                  "fsrcnn3": [r"models/FSRCNN_x3.pb", 3, "fsrcnn"],
                  "fsrcnn4": [r"models/FSRCNN_x4.pb", 4, "fsrcnn"],
                  "lapsrn2": [r"models/LapSRN_x2.pb", 2, "lapsrn"]}

    if model in model_dict:
        kv = model_dict[model]
        mpath, mname, mfactor = kv[0], kv[2], kv[1]

    sup_res = dnn_superres.DnnSuperResImpl_create()
    img = cv2.imread(img_path)
    sup_res.readModel(mpath)

    # sup_res.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # sup_res.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    sup_res.setModel(mname, mfactor)
    result = sup_res.upsample(img)

    img_name, image_dir = os.path.split(img_path)
    output_path = image_dir + r"\output" + "\\" + img_name
    cv2.imwrite(output_path, result)
