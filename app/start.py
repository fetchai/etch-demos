from flask import Flask, request, render_template
from collections import defaultdict
from utils.session import Session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")

# @app.route("/connect")
# def connect():
#     return render_template("connect.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/testresult", methods=['POST'])
def test_result():
    if request.method == 'POST':
        if session.is_connected():
            return f"Test connection is successful. You are currently connected " + \
                   f"to the {session.network} network, port {session.port}."
        else:
            return "You are not connected to a ledger. Please specify a network and try again."
    else:
        return "POST method failed. Please check Flask source."

@app.route("/deploy")
def deploy():
    return render_template("deploy.html")

@app.route("/deployresult", methods=['GET', 'POST'])
def deploy_result():
    if request.method == 'POST':
        # contract_name = request.form.get('etchname', False)
        # contract_text = str(request.form.get('etchvalue', False)).strip()
        contract_name = request.form['etchname'].strip()
        contract_text = request.form['etchvalue'].strip()
        # dir_path1 = "../demos/hello-world"
        # contract_name1 = "hello"
        # with open(f"{dir_path1}/{contract_name1}.etch", 'r') as file:
        #     contract_text1 = file.read()

        # print("CT: " + str(len(contract_text)))
        # print("CT1: " + str(len(contract_text1)))
        # print(len(contract_text.strip()))
        # print(len(contract_text))
        # print(len(contract_text1))
        # print(len(contract_text.count('\n')))
        # print(len(contract_text1.count('\n')))

        # if contract_text == contract_text1:
        #     print("pass")
        # else:
        #     print("fail")

        # print(contract_name)
        # print(contract_text)
        session.deploy(contract_name, contract_text)
        return f"Contract {contract_name}.etch has been deployed!"
        # if session.is_connected():
        #     return f"Success! You are conncted to the {session.network} " + \
        #            f"network, port {session.port}."
        # else:
        #     return "You are not connected to a ledger. Please specify a network and try again."
    else:
        return "POST method failed. Please check Flask source."

@app.route("/interact")
def interact():
    info_string = session.get_blockchain_info()
    contract_names = session.contracts.keys()
    # get funcnames
    function_names = []
    initial_ent_info = ""
    if len(contract_names) > 0:
        initial_name = list(contract_names)[-1]  # contract name that appears in select by default
        function_names = session.contracts[initial_name].funcs['query']  # default func type
        initial_ent_name = list(session.entities.keys())[-1]
        initial_ent_info = session.get_entity_info(initial_ent_name)

    return render_template("interact.html", status=info_string
                                          , contracts=session.contracts
                                          , initfuncnames=function_names
                                          , entities=session.entities
                                          , initentity=initial_ent_info
                          )

@app.route("/interactstatus", methods=['GET', 'POST'])
def interact_status():
    info_string = "Test123" # session.get_blockchain_info()
    return render_template('interact.html', status=info_string)
    # if request.method == 'POST':
    #     info_string = session.get_blockchain_info()
    #     request.form['statusspace'] = info_string
    #     return "Check the written etch file."
    #     # if session.is_connected():
    #     #     return f"Success! You are conncted to the {session.network} " + \
    #     #            f"network, port {session.port}."
    #     # else:
    #     #     return "You are not connected to a ledger. Please specify a network and try again."
    # else:
    #     return "POST method failed. Please check Flask source."

@app.route("/interactquery")
def interact_query():
    info_string = session.get_blockchain_info()
    contract_names = session.contracts.keys()
    # get funcnames
    function_names = []
    if len(contract_names) > 0:
        initial_name = list(contract_names)[-1]  # contract name that appears in select by default
        function_names = session.contracts[initial_name].funcs['query']  # default func type

    return render_template("interact.html", status=info_string
                                          , contracts=session.contracts
                                          , initfuncnames=function_names
                                          , entities=session.entities
                          )

@app.route("/executeresult", methods=['GET', 'POST'])
def execute_result():
    if request.method == 'POST':
        contract_name = request.form['contname'].strip()
        function_name = request.form['funcname'].strip()
        result = session.query(contract_name, function_name)
        return result
    else:
        return "POST method failed. Please check Flask source."

@app.route("/addresult", methods=['GET', 'POST'])
def add_result():
    if request.method == 'POST':
        entity_name = request.form['newname'].strip()
        session.add_entity(entity_name)
        return f"New Entity {entity_name} has been added."
    else:
        return "POST method failed. Please check Flask source."


if __name__ == "__main__":
    NETWORK = 'localhost'
    PORT = 8100
    session = Session(NETWORK, PORT)
    # session = Session(network=NETWORK, port=PORT)
    app.run(debug=True)
