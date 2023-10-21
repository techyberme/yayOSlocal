# yayOSlocal
## This a project about a streamlit-based web that enables the user to both monitor a kitchen appliance and check out the electricity prices
<img width="452" alt="image" src="https://github.com/techyberme/yayOSlocal/assets/107142731/d4b7e00d-993d-405b-a60e-9dc46065e1be">
 
Figure 2. 2

3.1 Web Page
From some time to now, electricity prices have risen considerably. A dishwasher can consume up to 730 Wh a cycle so turning it on when the electricity prices are low can be a great way to save money. This can definitely be an attractive catch for elders with a low monthly income. Even though electricity prices are available of the internet, they may not be easy to find, so a simple web in which the client can check out the prices and even turn on the dishwasher might be very useful to the client.
Additionally, the web includes a window in which the client may select the washing program from three different options and follow the time left to finish it.

Firstly, the app fetches data from an API called “preciodelaluz.org” wtich a code in JavaScript using the Node.js cross-platform. This API provides a great deal of data, but the program only fetches the time and price and saves it to a .csv file. In the code, the header with the names of the module is manually inserted and a for loop iterates a list containing the time interval so the code fetches the price for each time and uploads it to the data.csv file. 
As a result, we get a file like the following:
<img width="360" alt="image" src="https://github.com/techyberme/yayOSlocal/assets/107142731/f13db5a5-0fe6-4bc6-a63c-479abdb755a7">

Figure 2. 3
Secondly, this data is uploaded to a web page so the clients can get informed easily. In order to build the web, we have used Streamlit, a very popular open-source web builder based on the coding language Python.
In the code, we have used several libraries:
•	Pandas: A generalist library used for working with data file
•	CSV: Used to work with the .csv file.
•	Plotly.express: Allows to display data in interactive charts.
•	Hmac: Used to include an authentification form.

The aim of this app is to display the electricity prices so firstly, we will display the data from the .csv file in an interactive graph in which it is possible to check the data of a specific hour by simply putting the cursor on it. Additionally, we have added relevant information such as the average daily price and the maximum price.


<img width="360" alt="image" src="https://github.com/techyberme/yayOSlocal/assets/107142731/f410e9cc-a664-41da-8610-06e7025ee222">

Figure 2. 4

Moreover, we have used the web page to add some new features to the dishwasher so as to make it a smart item. We have added a section in which it is possible to choose the program and follow the time left for it to finish and a section where we can turn on the different appliances. It is also possible to turn on and off the appliances in the section "Aparatos".


<img width="360" alt="image" src="https://github.com/techyberme/yayOSlocal/assets/107142731/943d4a89-7cd1-4b46-bea0-94a59235438b">

Figure 2. 5

Finally, we added an authentication form so the web page is secured.

3.1.1 User’s monitorization
As parents get older, the worries of their sons and daughters of them having accident increases. Situations in which an elderly person suffers an accident and is not able to look for help are more common than desired. It is thus key to make out a way in which it is possible to know if everything is ok without needing an active role of the elderly person. A way to do so is to monitor their daily habits and raise an alarm if the actions of the client are not being the expected.
YayOS has come up with an easy solution: The dishwasher will transmit its status to the web page. For example, it will upload how many times it has been used so far in the day and whether the door is open or not. In this way, the family of the client can easily make sure he or she is fine without calling the person.

<img width="360" alt="image" src="https://github.com/techyberme/yayOSlocal/assets/107142731/db212476-21a0-469a-aadc-ad69cf23e09c"> 

Figure 2. 6

An example of the web can be found in the following link: https://abuelos.streamlit.app/
This web page has been made using Streamlit cloud and Github codespaces. Which work as servers for our online app. However, this tool has some limitations, so we have just uploaded a simple version of the final app.
