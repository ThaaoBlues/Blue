from flask import Flask, render_template, request, send_file, send_from_directory


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def config_page():
    return render_template("config_page.html")

@app.route("/action/<page>",methods=['GET', 'POST'])
def action(page):
    if page == "[ADD IROBOT CLEANER]":
        return render_template("add_irobot_cleaner.html")
    elif page == "[ADD WEBSITE VOICE COMMAND]":
        return render_template("add_custom_website.html")
    elif page == "[ADD CUSTOM VOICE COMMAND TO SEND TO A SERVER]":
        return render_template("add_custom_server.html")
    else:
        return page

@app.route("/process/<process_id>",methods=['GET','POST'])
def process(process_id):
    if process_id == "[ADD IROBOT CLEANER]":
        pass
    elif proces_id == "[ADD WEBSITE VOICE COMMAND]":
        pass
    elif proces_id == "[ADD CUSTOM VOICE COMMAND TO SEND TO A SERVER]":
        pass
    else:
        return render_template("config_page.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Tu t'es perdu je crois, fréro ya rien ici.", 404



if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")
