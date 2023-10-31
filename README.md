# html-compiler
Example shown; should be relatively straight forward.

place your fragments in the html_fragments folder, place your html pages in html_pages then run the command it will replace all of the {{ fragmentname.html }} with the contents of the fragment.

```
pip install .
```

Then you can either generate a new project
```
python -m HTMLCompiler generate .
```

Or specify one
```
python -m HTMLCompiler compile -t definition.toml
```

Here we can have the following fragments, pages and strings;

* html_fragments/header.html
```
<a>Hello</a>
<a>About</a>
<a>Contact</a>
```

* strings/welcome.json
```
{ "bio" : "test this" }
```

* html_pages/index.html
```
<!DOCTYPE html>
<head>

</head>
<body>
    {{ header.html }}
    <div>
        {{ welcome.bio }}
    </div>
</body>
```

At the moment it removes all the white space, since you won't be needing it in production.