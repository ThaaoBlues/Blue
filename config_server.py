from flask import Flask, render_template, request,abort,jsonify, send_file, send_from_directory, flash, redirect
from werkzeug.utils import secure_filename
from os import path
from util.res import *
from json import dumps, loads
import keyring
from util.res import *

UPLOAD_FOLDER = path.dirname(__file__)+'/skills_modules/'
ALLOWED_EXTENSIONS = {'py'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def config_page():
    return render_template("config_page.html")


@app.route("/action/<page>",methods=['GET', 'POST'])
def action(page):

    if page == "[MANAGE BLUE SKILLS]":
        with open("config/skills.blue","r") as f:
            modules = []
            for line in f.read().splitlines():
                modules.append(line.split(":")[0])
                sentences = line.split(":")[1]

        return render_template("manager_modules.html",modules=modules)

    elif page == "[ADD CREDS]":

        #display the page
        if request.method == "GET":
            return render_template("add_account.html",services= get_registered_services())
        
        #creation of a new account
        else:

            try:
                ac_service = request.form['service']
                ac_username = request.form['username']
                ac_password = request.form['password']
                keyring.set_password(ac_service,ac_username,ac_password)
                with open("config/accounts.blue","a") as f:
                    f.write(dumps({"service":ac_service,"username":ac_username})+"\n")
                    f.close()            
                    
                return render_template("success_message.html")

            except:
                return jsonify({"error": "malformed post request"})


    elif page == "[MANAGE CREDS]":

        return render_template("manage_accounts.html")


    elif page == "[ADD WEBSITE VOICE COMMAND]":
        return render_template("add_custom_website.html")

    elif page == "[ADD CUSTOM VOICE COMMAND TO SEND TO A SERVER]":
        return render_template("add_custom_server.html")

    elif page == "[ADD RSS FEED]":
        return render_template("add_rss_feed.html")

    elif page == "[ADD BLUE SKILL]":
        return render_template("add_skill.html")

    elif page == "[MANAGE RSS FEED]":
        with open("config/custom_rss_feed.blue","r") as f:
            feeds = []
            for line in f.read().splitlines():
                try:
                    feeds.append(loads(line))
                except Exception as e:
                    print(e)
                    
            f.close()

        return render_template("manage_rss_feed.html",feeds=feeds,lenght=len(feeds))
    
    
    elif page == "[MANAGE WEBSITE VOICE COMMAND]":
        with open("config/custom_websites.blue","r") as f:
            array = [""]
            name = [""]
            a = f.read().split("\n")
            i=0
            for line in range(0,len(a)):
                print(a[line])
                if line%2==0:
                    array.append(a[line]+"||")
                    name.append(a[line])
                    i+=1
                else:
                    array[i] += a[line]


        return render_template("manage_custom_website.html",lenght=len(array),array=array,name=name)
    

    elif page == "[ADD REMINDER]":

        if request.method == "GET":

            return render_template("add_reminder.html")
        else:
            
            try:
                w = request.form['week']
                #this is a date based reminder

                return render_template("success_message.html")

            except:

                #this is a wake-up alarm
                add_wake_up_alarm(str(request.form['date']).split("-")[2],request.form['time'],request.form["wakeup_music"])
                return render_template("success_message.html")
                

            
    elif page == "[MANAGE REMINDERS]":
        pass

    else:
        return abort(404)




@app.route("/process/<process_id>",methods=['GET','POST'])
def process(process_id):

    if process_id == "[ADD BLUE SKILL]":

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(app.config['UPLOAD_FOLDER']+ filename)

            with open("/skills/skills.blue","a") as f:
                f.write(path.extsep(filename)[0]+":"+request.form['voice_command'])

            return render_template("success_message.html")

    elif process_id == "[DELETE ACCOUNT]":
        ac_service = request.args.get("service")
        username = keyring.get_credential(ac_service)
        password = keyring.get_password(ac_service,username)
        keyring.delete_password(ac_service,username,password)

        return render_template("success_message.html")

        
    
    elif process_id == "[ADD RSS FEED]":
        voice_command = str(request.form['command']).lower()
        url = request.form['url']
        with open("config/custom_rss_feed.blue","a") as f:
            f.write(dumps({"url" : url,"command" : voice_command}))
            f.close()

        return render_template("success_message.html")

        
    elif process_id == "[ADD WEBSITE VOICE COMMAND]":

        voice_command = str(request.form['command']).lower()
        url = request.form['url']

        with open("config/custom_websites.blue","a") as f:
            f.write(f"{voice_command}\n{url}\n")
            f.close()

        return render_template("success_message.html")

    elif process_id == "[ADD CUSTOM VOICE COMMAND TO SEND TO A SERVER]":

        ip = request.form['ip_addr']
        port = request.form['port']
        voice_command = str(request.form['command']).lower()
        message = str(request.form['msg']).replace("\n","[NL]")

        with open("config/custom_servers.blue","a") as f:
            f.write(f"{voice_command}\n{ip}\n{port}\n{message}\n")
            f.close()

        return render_template("success_message.html")



    elif "[MANAGE WEBSITE VOICE COMMAND]" in process_id:
        name = process_id.replace("[MANAGE WEBSITE VOICE COMMAND]","")
        with open("config/custom_websites.blue","r") as f:
            tt = f.read().split("\n")
            print(tt)
            for ele in tt:
                if ele == name:
                    tt.pop(tt.index(name))
                    tt.pop(tt.index(name)+1)
        
        with open("config/custom_websites.blue","w") as f:
            for ele in tt:
                f.write(str(ele) + "\n")
            f.close()

        return render_template("success_message.html")

    elif "[DELETE RSS FEED]" in process_id:
        
        id = request.args.get("feed_id")
        with open("config/custom_rss_feed.blue","r") as f:
            feeds = f.read().split("\n")
            feeds.pop(int(id))
 
        with open("config/custom_rss_feed.blue","w") as f:
            for feed in feeds:
                f.write(str(feed) + "\n")

            f.close()

        return render_template("success_message.html")

    elif process_id == "[MANAGE CUSTOM VOICE COMMAND TO SEND TO A SERVER]'":
        return render_template("success_message.html")

    else:
        return render_template("config_page.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Tu t'es perdu je crois, fréro ya rien ici.", 404



def start_webserver():
    app.run(host="0.0.0.0",port="80")


