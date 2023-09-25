# WHM-automation

An automation tool that interacts with Marcel's server

## Built With

- Flask
- Selenium

## Getting Started

- **To get a local copy of the repository please run the following commands on your terminal:**
  Clone the project
  ```
  git clone https://github.com/LegacyNetworkAG/WHM-automation.git
  ```
  Navigate into the directory
  ```
  cd WHM-automation
  ```
  Create a virtual environment if you don't have one.
  ```
  python3 -m venv venv
  ``` 
  Activate the virtual environment
  ```
  source venv/bin/activate
  ```
  Install the project dependencies
  ```
  pip install -r requirements.txt
  ```

- **Please run the following commands on your terminal to start the app:**
 Set the flask app environ
  ```
  export FLASK_APP=src/server.py
  ```
  Start the server
  ```
  flask run
  ```

## App Endpoints
Open your API testing tool and hit this endpoint
- GET: `/api/v1/marcel/login` to login into the marcel server.


## Test The Automation
- ***Please note that you should have a Chrome browser installed before trying this out***. </br>
The snippet code below enables a headless call to the Chrome browser. </br>
This basically means that the browser is hidden by default. 
```
self.options.add_argument('headless')
```
However, you can navigate to the ```marcel.py``` file inside the ```src/app/platforms``` directory and
comment the code snippet by add a ```#``` character in order to see the full automation on the browser. 
See example below:
```
# self.options.add_argument('headless')
```

- **After commenting the code snippet, run the following commands on your terminal to start the automation:**
  - Goto the root of the project ie.: ```YOUR_FILE_PATH/WHM-automation/```
  - Run the following and see the automation.
  ***Please note that you can use ```python``` or ```python3``` in the commands. It's based on what you have installed.***
  ```
  python3 src/runner.py
  ```
  - Kill ```ctrl + c``` the terminal after to close the session. <br />


 Final Note: ***Please uncomment the code snippet that you commented above before testing out the endpoints.***

  
## Authors

👤 **Muhammad Sesay**

- GitHub: [@mmsesay](https://github.com/mmsesay)
- Twitter: [@DeeMaejor](https://twitter.com/DeeMaejor)
- LinkedIn: [LinkedIn](https://linkedin.com/in/muhammad-m-sesay)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments
