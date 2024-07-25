**HTML**
Hyper Text Markup Language, interpretable code and a language for encoding webpages

**CSS**
Cascading Style Sheets, used to specify style of a webpages

**REST**
Representative State Architecture

**CRUD**
CREATE, READ, UPDATE, DELETE
The four basic operations of persistent storage, such as databases

**JavaScript**
A programming language, usually used for dynamically rendering or altering webpage content

**Cookies** 
Small piece of data sent from a server to the user's browsers

**HTTP Requests/Responses**
REQUESTS: a message sent from the client to initiate an action in the server
		POST(or GET, HEAD, OPTIONS) /URL HTTP/version
RESPONSES: a status response from the server back to the client

**Fixtures**
- the test context

**Assert**
- Checking whether the outcome is the same as expected out of the test case

**Stub**
- Canned answers, a test oduble

**Selenium**
- Testing software

**Coverage**
- How well does it cover all the possible aspects in the software, would it capture every possible.

**DOM**
- Document Object Model

**Prototypes**
- A prototype is the way that JS object oriented programming works, it allows objects to inherit features from one another

**Inheritance**
- A prototype inheritance allows for a new prototype to gain the features from the parent prototype whilst being able to add and alter features. 

## Differences between agile and trad
- Constant communication with the client, deliverables being shown on a regular basis
- Short iterations
- Design, Test, Code, Refactor
- Prototypes

## HTML vs HTTP
- Hyper Text Markup Language : interpretable text for browsers, 
	a language for encoding webpages
- Hyper Text Transfer Protocol : protocol for request and response packages to be 
	transfered according to REST principles
	
## REST
- Representative State Architecture
1. Client-Server Model
2. Layered System
3. Cache
4. Code on Demand
5. Stateless
6. Uniform Interface

## Appearance and Style of a Page
- Text colour is black for the whole page and yellow background
- white background for the Server

## "The web was designed to be scalable and robust, but it was not designed to be secure" Discuss in terms of the 6 characteristics of REST
- Client-Server model: can add more servers to allow for expanded need
- Cache allows for record of browsing history
- Code on demand allows for remote servers to provide code, however this can be 
	malicious
- Layered, so man in the middle attacks are possible

## 6 Key Architectural Constraints of REST software 
1. Cache
2. Client-server Model
3. Code on Demand
4. Layered
5. Uniform Interface 
6. Stateless

## Process of registering a new user account using a Flask applications
- Request register page with HTTP GET request to get route
- Form is rendered, HTML served as response
- Form filled by user
- HTTP POST request sends to register route
- Form validator confirms
- Checks database
- Hash PW
- Add user data to database
- Redirect user to login (GET HTML object)

## Schema Description
**Students Table**
- Columns: first_name, surname, project_id
- Many to one with project table, joined via project_id
**projects Table**
- Columns: project_id, Description, team
- Team is a python list of students that are doing that project

## Schema 2
**User**
username (String(64), primary_key = True), password (hashed) (db.String(64)), profile_pic
One to many with Post and Comment
**Post**
username (db.String(64)), description, checkbox (db.Integer)
Many to One with user
One to many with Comment
**Comment**
username, content, date
Many to one with user
Many to one with post

## Differences between server and client side rendering
- Flask is server side rendering: the code is sent to the client dynamically from 
the server, this means that the HTML is pre-rendered, meaning a faster experience for 
the user
- REST, API, AJAX and jQuery is client side: the HTML is dynamically rendered by the client, 
however, this means that the initial content is minimal, lowering searchability

## Dir Structure of a typical Flask project
App
	__init__.py
	main
		\_\_init\_\_.py
		routes.py
	models
		...
	templates
		base.HTML
		...
	static
		style.CSS
		


## Main activities of an agile web dev Process
**different roles people have**
- 
**how application requirements are gathered and maintained**
- Requirements listened to from client, listed
- When requirements are met, deliverables are shown to the client for feedback
- 

## JS Event Handlers
```js
button.addEventListener('click', event)
```
- can also be added by inline `onclick`
```js
let btn = document.querySelector('#btn');
btn.onclick = function() {
	alert('aughegh');
}
```

The HTML inline method, whilst the easiest to implement, leads to unmaintainable code and the inability to reuse code for other elements on the web page. 

