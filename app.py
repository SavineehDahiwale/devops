from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL exam"


@app.route("/modules", methods=["GET"])
def modules():
    return "Ditiss module list :-"
    return "Compliance Audit"
    return "Public key Infrastructure"
    return "Concept of Operating system & Administration"
    return "Fundamentals of Computer Networking"
    return "Network Defence & Countermeasures"
    return "Cyber Forensics"
    return "Security Concepts"
    return "ItIL & Devops"

@app.route("/me", methods=["GET"])
def name():
    return "Name :- Savinesh Dahiwale"
    return "PRN :- 230344223044"
    return "Phone No :- 7350390313"


# run the application
app.run(host="0.0.0.0", port=4000, debug=True)

