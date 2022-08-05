# Flask App Checklist
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
```
User Snippet: servflask
```

### Paste into index.html:
```
User Snippet: bootshtml

In <head></head> and before <title></title>:
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

## To view in Browser:
head to Local Host bookmark
