
import pandas
from sklearn.tree import DecisionTreeClassifier
import json
from twilio.rest import Client
import pyttsx3
import warnings
warnings.filterwarnings('ignore')


def main():
    data = pandas.read_csv("/Users/xy0ke/Desktop/godly/SmartHealtCare/SmartHealth/patients.csv")


    X = data[['ax','ay','az','gx','gy','gz']]
    y = data['target']

    set = DecisionTreeClassifier()
    set.fit(X, y)

    pred = set.predict([[-612, -1028, 17008, -60, 41, -308]])

    # pred = 1
    print(int(pred))

    if int(pred) == 1:
        print('Emgergency: Car Crash Detected\nCalling..')

        # engine = pyttsx3.init()
        # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.veena')   
        # engine.say("Emergency")
        # engine.runAndWait()
        # engine.stop()


        f = open('emergency.json')
        j = json.load(f)
        f.close()

        account_sid = '<account_sid>'
        auth_token = '<auth_token>'

        for pepol in j:
            ph = j[pepol].key()

	        client = Client(account_sid, auth_token)

	        call = client.calls.create(
	                                url='https://xy0ke.me/voice.xml',
	                                to=phno,
	                                from_='+13344381751')

	        print(call.sid)
    else:
        print('Normal')


if __name__ == '__main__':
    main()