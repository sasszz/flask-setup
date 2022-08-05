# Flask App Checklist
## Flask App Folder Tree Diagram
<img src="flask-folder-tree.png" alt="Flask Folder Tree Diagram" height=200px>

## Making the Root folder

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

## Paste into server.py:
- <em> SEE PYTHON FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
```
User Snippet: servflask
```

## Paste into index.html:
- <em> SEE PYTHON FILE IN REPO FOR DOCUMENT TEMPLATE </em>
- <em> SEE JSON FILE FOR SNIPPET </em>
```
User Snippet: bootshtml
```

<em>In <head></head> and before <title></title>:</em>

```
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
```

## In terminal - run:
```
python3 server.py
```

<em>To view in Browser:</em>
```
head to Local Host bookmark and include root slash if specifiec
```
