## Deploying ML Model using Flask
This is a simple project to elaborate how to deploy a Machine Learning model using Flask.
### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask installed.

### Project Structure
This project has four major parts :
1. ml.py - This contains code fot our Machine Learning model to detect fake news absed on trainign data in 'FA-KES-Dataset.csv' file.
2. main.py - This contains Flask APIs that receives the news through GUI or API calls, computes the cridibility of the news based on our model and returns it.
3. template - This folder contains the HTML template (index.html) to allow user to enter the news and displays wether this news are real or fake.
4. static - This folder contains the css folder with style.css file which has the styling required for out index.html file.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command from command prompt -
```
python ml.py
```
This would create a serialized version of our model into a file "clf.joblib"

2. Run main.py using below command to start Flask API
```
python main.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter text value in input box and hit Detect.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
check the output here: http://127.0.0.1:5000/predict

4. In case you want to deploy this model on Google Cloud using App Engine as I did, I added two files to be able to do that "requirements.txt" and "app.yaml" which they have the required librares to be installed and the configuration to be worked on the Cloud with minimal resources.

