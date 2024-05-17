# pylint: skip-file
from flask import Blueprint, make_response
from flask import request, jsonify
from controller.modelCotroller import ControllerModel
import json
from flask import Response
import pandas as pd

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/diabetes', methods=['POST', 'OPTIONS'])
def diabetes():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            pregnancies = int(request.form['Pregnancies'])
            glucose = float(request.form['Glucose'])
            blood_pressure = float(request.form['BloodPressure'])
            skin_thickness = float(request.form['SkinThickness'])
            insulin = float(request.form['Insulin'])
            bmi = float(request.form['BMI'])
            diabetes_pedigree_function = float(request.form['DiabetesPedigreeFunction'])
            age = int(request.form['Age'])

            to_predict_list = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
            result = ControllerModel.DiabetesPredictor(to_predict_list)

            result_data = {
                'Data': {"Result" : result[0].tolist(), "Probability": result[1].tolist()},
                'success': True,
                'message': "Successful"
            }
            response = Response(json.dumps(result_data), status=200, content_type='application/json')
            return response

        except Exception as e:
            print(f"An error occurred in route: {e}")
            return jsonify({'success': False, 'message': 'An error occurred'}), 500

@lab_bp.route('/kidney', methods=['POST', 'OPTIONS'])
def kidney():
    try:
        if request.method == 'OPTIONS':
            # Handle preflight request
            response = Response()
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'POST')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            return response

        if request.method == 'POST':
            form_data = request.form
            print(form_data)
            age = int(form_data['Age'])
            bloodPressure = float(form_data['BloodPressure'])
            specificGravity = float(form_data['SpecificGravity'])
            albumin = float(form_data['Albumin'])
            sugar = float(form_data['Sugar'])
            redBloodCells = int(form_data['RedBloodCells'])
            pusCell = int(form_data['PusCell'])
            pusCellClumps = int(form_data['PusCellClumps'])
            bacteria = int(form_data['Bacteria'])
            bloodGlucoseRandom = float(form_data['BloodGlucoseRandom'])
            bloodUrea = float(form_data['BloodUrea'])
            serumCreatinine = float(form_data['SerumCreatinine'])
            sodium = float(form_data['Sodium'])
            potassium = float(form_data['Potassium'])
            haemoglobin = float(form_data['Haemoglobin'])
            packedCellVolume = float(form_data['PackedCellVolume'])
            whiteBloodCellCount = float(form_data['WhiteBloodCellCount'])
            redBloodCellCount = float(form_data['RedBloodCellCount'])
            hypertension = int(form_data['Hypertension'])
            diabetesMellitus = int(form_data['DiabetesMellitus'])
            coronaryArteryDisease = int(form_data['CoronaryArteryDisease'])
            appetite = int(form_data['Appetite'])
            print("hiii")
            pedaEdema = 0
            aanemia = int(form_data['Anemia'])

            to_predict_list = [[age, bloodPressure, specificGravity, albumin, sugar, redBloodCells, pusCell, pusCellClumps, bacteria, bloodGlucoseRandom, bloodUrea, serumCreatinine, sodium, potassium, haemoglobin, packedCellVolume, whiteBloodCellCount, redBloodCellCount, hypertension, diabetesMellitus, coronaryArteryDisease, appetite, pedaEdema, aanemia]]
            print(to_predict_list)
            size = len(to_predict_list[0])
            result = ControllerModel.KidneyPredictor(to_predict_list, size)
            result_data = {
                'Data': {"Result": result[0].tolist(), "Probability": result[1].tolist()},
                'success': True,
                'message': "Successful"
            }
            response = Response(json.dumps(result_data), status=200, content_type='application/json')
            return response

    except Exception as e:
        print(f"An error occurred in route: {e}")
        return None


@lab_bp.route('/liver', methods=['POST', 'OPTIONS'])
def liver():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            form_data = request.form
            print(form_data)
            age = int(form_data['age'])
            totalBilirubin = float(form_data['totalBilirubin'])
            directBilirubin = float(form_data['directBilirubin'])
            alkalinePhosphotase = float(form_data['alkalinePhosphotase'])
            alamineAminoTransFerase = float(form_data['alamineAminoTransFerase'])
            totalProtiens = float(form_data['totalProtiens'])
            albumin = float(form_data['albumin'])
            albuminAndGlobulinRatio = float(form_data['albuminAndGlobulinRatio'])
            genderMale = False
            genderFemale = True
            if(form_data['gender'] == 'male'):
                genderMale = True
                genderFemale = False
            features_to_merge = pd.Series([ directBilirubin,alamineAminoTransFerase])
            merged_feature = features_to_merge.mean()
            to_predict_list = [[age, totalBilirubin, alkalinePhosphotase, totalProtiens,albumin,albuminAndGlobulinRatio, genderFemale, genderMale, merged_feature]]
            size = len(to_predict_list[0])
            result = ControllerModel.LiverPredictor(to_predict_list, size)
            return jsonify({'Data': {"Result" : result[0].tolist(), "Probability":result[1].tolist()}, 'success':True, 'message':"Successful"}), 200

        except Exception as e:
            print(f"An error occurred in route: {e}")
            return None

@lab_bp.route('/hepetitis', methods=['POST', 'OPTIONS'])
def hepatitis():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            form_data = request.form
            print(form_data)
            age = int(form_data['Age'])
            alb = float(form_data['ALB'])
            alp = float(form_data['ALP'])
            alt = float(form_data['ALT'])
            ast = float(form_data['AST'])
            bil = float(form_data['BIL'])
            che = float(form_data['CHE'])
            chol = float(form_data['CHOL'])
            crea = float(form_data['CREA'])
            ggt = float(form_data['GGT'])
            prot = float(form_data['PROT'])
            sex = 0
            if form_data['sex'].lower() == 'male':
                sex = 1
            to_predict_list = [[age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]]
            size = len(to_predict_list[0])
            result = ControllerModel.HepetitisPredictor(to_predict_list, size)
            result_data = {
                'Data': {"Result": result[0].tolist(), "Probability": result[1].tolist()},
                'success': True,
                'message': "Successful"
            }
            response = Response(json.dumps(result_data), status=200, content_type='application/json')
            return response

        except Exception as e:
            print(f"An error occurred in route: {e}")
            return jsonify({'success': False, 'message': 'An error occurred'}), 500




@lab_bp.route('/lungs', methods=['POST', 'OPTIONS'])
def lungs():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            form_data = request.form
            print(form_data)
            age = int(form_data['age'])
            smoking = int(form_data['smoking'])
            yellow_fingers = int(form_data['yellow_fingers'])
            anxiety = int(form_data['anxiety'])
            peer_pressure = int(form_data['peer_pressure'])
            chronic_disease = int(form_data['chronic_disease'])
            fatigue = int(form_data['fatigue'])
            allergy = int(form_data['fatigue'])
            wheezing = int(form_data['wheezing'])
            alcohol_consuming = int(form_data['alcohol_consuming'])
            coughing = int(form_data['coughing'])
            swallowing_difficulty = int(form_data['swallowing_difficulty'])
            chest_pain = int(form_data['chest_pain'])

            to_predict_list = [[age,smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, swallowing_difficulty, chest_pain]]

            # Convert NumPy integers to Python integers
            to_predict_list = [[int(x) for x in sublist] for sublist in to_predict_list]

            result = ControllerModel.lungsPredictor(to_predict_list, 13)
            ans = []
            ans.append(int(result[0]))
            print("result is" , result)
            result_data = {
                'Data': {"Result": ans, "Probability": result[1].tolist()},
                'success': True,
                'message': "Successful"
            }
            response = Response(json.dumps(result_data), status=200, content_type='application/json')
            return response

        except Exception as e:
            print(f"An error occurred in route: {e}")


@lab_bp.route('/heart', methods=['POST', 'OPTIONS'])
def heart():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            form_data = request.form
            print(form_data)
            age = int(form_data['age'])
            sex = int(form_data['sex'])
            cp = int(form_data['cp'])
            trtbps = float(form_data['trtbps'])
            chol = float(form_data['chol'])
            fbs = int(form_data['fbs'])
            restecg = int(form_data['restecg'])
            thalachh = float(form_data['thalachh'])
            exng = int(form_data['exng'])
            oldpeak = float(form_data['oldpeak'])
            slp = int(form_data['slp'])
            caa = int(form_data['caa'])
            thall = int(form_data['thall'])

            to_predict_list = [[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]
            result = ControllerModel.HeartPredictor(to_predict_list, len(to_predict_list[0]))
            result_data = {
                'Data': {"Result": result[0].tolist(), "Probability": result[1].tolist()},
                'success': True,
                'message': "Successful"
            }
            response = Response(json.dumps(result_data), status=200, content_type='application/json')
            return response

        except Exception as e:
            print(f"An error occurred in route: {e}")
            return jsonify({'success': False, 'message': 'An error occurred'}), 500
