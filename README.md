# FaceRecognition-attendance-machine
This model recognizes face and marks attendance on a csv file and uploads the attendance on a local server and it has some additional features also.
# Face-Recognition-based-Attendance

A program to take attendance of a person using face recognition.

## Getting Started

Use GUI_color.py or GUI_background.py or GUI.py to run.

### Prerequisites

What things you need to run the software.

To install modules run:

```
pip install -r requirements.txt
```

Modules which will be installed includes:
```
    face_recognition
    opencv-python
    pandas
```


### Instructions

The major program files being used are:
```
    1.Registation.py
    2.Taking Attendance.py
    3.Deleting.py 
```

#### 1.Registeration.py
This program takes id and name as input,then takes 2 images of the user and save the encodings along with details.
Note:The code for taking images is selfie.py which is imported in this program.

For example:

If inputs are : 
```
Id=1
Name=vineet
```                

Then it will take 2 images of vineet, and save ([encodings of both images],[id two times],[name two times]) as a tuple
and store it in a data.dat file.

example tuple:
```
(array[[encoding of 1st image][encoding of 2nd image]],array[1,1],array["vineet","vineet"])
```

Two images are used to increase accuracy.

You can check whats inside the data.dat file using testing_reading.py file (optional).

#### 2.Taking Attendance.py
Note:This program is currently incomplete, it doesn't save the attendance to .csv file right now.

This program uses data.dat file to load encodings and details.
Use those encodings to match faces from webcam.
If matched, it is supposed to take the attendance of that person if he's/she's in the database (i.e. data.dat file),
or it will show unknown and close the window after a few seconds.

#### 3.Deleting.py (optional)
This program deletes the encodings and details of a person from the database (i.e. data.dat file).

It also creates a backup of data.dat file as it was, before deleting the id.
The backup is stored as data_last_backup.dat.

Note:Keep in mind that the backup is only the data.dat file before 1 change (1 deletion),
     You can not get the initial data.dat backup after 2 changes (more than 1 deletion).




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

Team members:
```
Peeyush(Leader)
Nitish
Razaul
Sourav
Rahul
Vineet
```

