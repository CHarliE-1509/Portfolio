from flask import Flask,render_template,request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/sample")
def sample():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("Form.html")

@app.route("/upload", methods= ["GET","POST"])
def upload():
    if request.method == "POST":
        e_mail=request.form.get("email")
        fullName=request.form.get("fullName")
        Title_1=request.form.get("title_1")
        Title_2=request.form.get("title_2")
        Title_3=request.form.get("title_3")
        Aspire=request.form.get("Asp")
        PhoneNumber=request.form.get("PhoneNumber")
        Address=request.form.get("Address")
        Experience01=request.form.get("Experience01")
        CA01=request.form.get("CA01")
        Dur01=request.form.get("D1")
        Co01=request.form.get("Company01")
        Experience02=request.form.get("Experience02")
        Co02=request.form.get("Company02")
        Dur02=request.form.get("D2")
        CA02=request.form.get("CA02")
        Univeristy01=request.form.get("UNI1")
        Univeristy02=request.form.get("UNI2")
        Grade1=request.form.get("G1")
        Grade2=request.form.get("G2")
        Education01=request.form.get("Education01")
        Education02=request.form.get("Education02")
        Education03=request.form.get("Education03")
        Education04=request.form.get("Education04")
        BItools=request.form.get("BI")
        Cer01=request.form.get("Cer01")
        Cer02=request.form.get("Cer02")
        Cer03=request.form.get("Cer03")
        Cer04=request.form.get("Cer04")
        Skill01=request.form.get("Skill01")
        Skill02=request.form.get("Skill02")
        Skill03=request.form.get("Skill03")
        Skill04=request.form.get("Skill04")
        Skill05=request.form.get("Skill05")
        Skill06=request.form.get("Skill06")
        Skillscore01=request.form.get("Skillscore01")
        Skillscore02=request.form.get("Skillscore02")
        Skillscore03=request.form.get("Skillscore03")
        Skillscore04=request.form.get("Skillscore04")
        Skillscore05=request.form.get("Skillscore06")
        Gskills=request.form.get("Gen_Skills")
        Project01=request.form.get("Project01")
        Project02=request.form.get("Project02")
        Project03=request.form.get("Project03")
        Project04=request.form.get("Project04")
        Pro01Desc=request.form.get("Pro01Desc")
        Pro02Desc=request.form.get("Pro02Desc")
        Pro03Desc=request.form.get("Pro03Desc")
        Pro04Desc=request.form.get("Pro04Desc")
        LinkedinID=request.form.get("LinkedinID")
        GithubID=request.form.get("GithubID")
        interest=request.form.get("Interest")
        Bio=request.form.get("Bio")
        WBio=request.form.get("WorkBio")

        print(e_mail,fullName)

    return render_template("index.html", em=e_mail,fname=fullName,T1=Title_1,T2=Title_2,
                            T3=Title_3,asp=Aspire,github=GithubID,addrs=Address,S1=Skill01,
                            S2=Skill01,S3=Skill03,S4=Skill04,S5=Skill05,
                            Score1=Skillscore01,Score2=Skillscore02,Score3=Skillscore03,
                            Score4=Skillscore04,Score5=Skillscore05,BIO=Bio,edu1=Education01,
                            edu2=Education02,BI=BItools,GS=Gskills,INTEREST=interest,LI=LinkedinID,short_bio=WBio
                            ,D1=Dur01,D2=Dur02,exp01=Experience01,exp02=Experience02,ORG01=Co01,ORG02=Co02,U1=Univeristy02,
                            U2=Univeristy02,GR1=Grade1,GR2=Grade2,Co_about_01=CA01,Co_about_02=CA02,P1=Project01,PD1=Pro01Desc,
                            P2=Project02,PD2=Pro02Desc,P3=Project03,PD3=Pro03Desc,P4=Project04,PD4=Pro04Desc,pho_num=PhoneNumber)

    return("Uploaded")


app.run(debug=False) 
