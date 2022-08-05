# Flask App Checklist
## Flask App Folder Tree Diagram
<img src="flask-folder-tree.png" alt="Flask Folder Tree Diagram" height=200px>

## Making the Root folder
#### Notes:
- some commands may be MAC-specific
- "flask_dir" = the name of your Flask App folder
- "touch" on MAC creates a file
- "cd" steps into the next folder
- "cd .." steps back one folder
#### In terminal - run:

```
mkdir flask_dir 
cd flask_dir 
```
```
mkdir templates 
cd templates
touch index.html
cd ..
```
```
mkdir static
cd static
touch style.css
touch script.js
cd .. 
```
```
pipenv install flask 
```
```
touch server.py 
```
Open VS Code:
```
code .
```

## Paste into server.py:
- <em> SEE PYTHON FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
- User Snippet: 
```
servflask
```

## Paste into index.html:
- <em> SEE HTML FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
- User Snippet: 
```
bootshtml
```
#### If using User Snippet, proceed here:
- The proper way to link Javascript, CSS and images in a Flask HTML file
- <em>In the HEAD section and before TITLE:</em>
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
```
python3 server.py
```

<em>To view in Browser</em>, head to
```
http://localhost:5000/
```
## To exit Virtual Environment
#### In terminal - run:
```
CTRL + C
```
