from flask import *  
import sqlite3
import cv2
import time
  
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html");  # display template

@app.route("/home")
def home():
    return render_template("home.html");  # display template
 
@app.route("/add")
def add():  
    return render_template("add.html")  
#
# def datasetScript():
#     # url:({{url_for("http://localhost:5000/add")}});
#     exec("python face_datasets.py")


@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            gender = request.form["gender"]  
            department = request.form["department"]
            with sqlite3.connect("emp.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email, gender,department) values (?,?,?,?)",
                            (name,email,gender,department))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
              


@app.route("/view")  
def view():  
    con = sqlite3.connect("emp.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("emp.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)

@app.route("/faced", methods=['POST'])
def faced():
    print("hello")
    exec(open("face_datasets.py").read())
    # exec(open("training.py").read())

@app.route("/viewed", methods=['POST'])
def viewed():
        print("hello")
        exec(open("face_recognition.py").read())





    #
    # # Import OpenCV2 for image processing
    #
    # # Start capturing video
    # vid_cam = cv2.VideoCapture(0)
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    #
    # # Detect object in video stream using Haarcascade Frontal Face
    # face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #
    # # For each person, one face id
    # face_id = 2  # for multiple person different ids
    #
    # # Initialize sample face image
    # count = 0
    #
    # # Start looping
    # while (True):
    #
    #     # Capture video frame
    #     _, image_frame = vid_cam.read()
    #
    #     # Convert frame to grayscale
    #     gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    #
    #     # Detect frames of different sizes, list of faces rectangles
    #     faces = face_detector.detectMultiScale(gray, 1.3, 5)
    #
    #     # Loops for each faces
    #     for (x, y, w, h) in faces:
    #         # Crop the image frame into rectangle
    #         cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #
    #         # Increment sample face image
    #         count += 1
    #
    #         # Save the captured image into the datasets folder
    #         cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
    #
    #         # Display the video frame, with bounded rectangle on the person's face
    #     cv2.imshow('Frame', image_frame)
    #
    #     # To stop taking video, press 'q' for at least 100ms
    #     if cv2.waitKey(100) & 0xFF == ord('q'):
    #         break
    #
    #     # If image taken reach 100, stop taking video
    #     elif count > 100:
    #         break
    #
    # # Stop video
    # vid_cam.release()
    #
    # # Close all started windows
    # cv2.destroyAllWindows()
    # msg="Lolllllllll"
    # return render_template("hi.html",msg = msg)


if __name__ == "__main__":
    app.run()  
