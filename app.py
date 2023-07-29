from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL exam"


@app.route("/modules", methods=["GET"])
def modules():
    return "Ditiss module list :- ItIL & Devops,Security Concepts,Cyber Forensics,Network Defence & Countermeasures,Fundamentals of Computer Networking,Concept of Operating system & Administration,Public key Infrastructure,Compliance Audit"


@app.route("/me", methods=["GET"])
def name():
    return "Name :- Savinesh Dahiwale, Phone No :- 7350390313, PRN :- 230344223044"


# run the application
app.run(host="0.0.0.0", port=4001, debug=True)

