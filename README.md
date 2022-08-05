# Flask App Checklist
## Flask App Folder Tree Diagram
<img src="flask-folder-tree.png" alt="Flask Folder Tree Diagram" height=200px>

## Making the Root folder
#### In terminal - run:
("flask_dir" = the name of your Flask App folder)

```
mkdir flask_dir 
```
(changes directory to the Flask App folder just created)
```
cd flask_dir 
```
(templates folder will contain HTML)

```
mkdir templates 
cd templates
```
(MAC - creates an HTML file)
```
touch index.html
```
(IMPORTANT: exit templates folder into main directory so we can add another folder)
```
cd ..
```
(static folder will contain CSS, Javascript and Images)
```
mkdir static
cd static
```
(MAC - creates a CSS and Javascript files)
```
touch style.css
touch script.js
```
(IMPORTANT: exit static folder into main directory so we can install Flask)
```
cd .. 
```
(installs Flask in main Flask App folder)
```
pipenv install flask 
```
(MAC - creates a Python file)
```
touch server.py 
```

## Paste into server.py:
- <em> SEE PYTHON FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
User Snippet: 
```
servflask
```

## Paste into index.html:
- <em> SEE HTML FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
User Snippet: 
```
bootshtml
```
#### If using User Snippet, proceed here:
<em>In HEAD section and before TITLE:</em>
(the proper way to link Javascript, CSS and images in a Flask HTML file)

```
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
```

## Initiating the server
#### In terminal - run:
(note "python3" is for MAC)
```
python3 server.py
```

<em>To view in Browser:</em>
```
Head to http://localhost:5000/ (bookmark) include root slash if specified
```
## To exit Virtual Environment
#### In terminal - run:
(note command may work for MAC only)
```
CTRL + C (MAC)
```
