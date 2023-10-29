# html-compiler
Example shown; should be relatively straight forward.

place your fragments in the html_fragments folder, place your html pages in html_pages then run the command it will replace all of the {{ fragmentname.html }} with the contents of the fragment.

```
python compiler.py html_fragments html_pages test_out strings
```

At the moment it removes all the white space, since you won't be needing it in production.