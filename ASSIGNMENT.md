# Take-home Assignment

Build a small Python library with the following functionality:

1. Read in a PDF from a local path and encode in some way as a Python object.
2. Be able to extract the sum of the values in the displayed line items for the attached forms.
3. Make a short development plan for additional features you would implement if you had more time.

Note - we will test your library against PDFs that may be a bit fishier than the ones shown here (but the form template will remain the same). So try to add some robustness to your extraction.

You can use whatever libraries you like. Please upload the result to GitHub in a public repo and let us know where to find it. Be sure to commit often as you develop - we will check out the commit history to see how you iterate on your ideas!

If you have extra time feel free to add more bells and whistles, e.g.

- Documentation done
- Tests done
- Extract each individual line item, not just the sum. done
- Make your extraction logic more generic - does it work if the names of the line items are changed? Can it handle malformed inputs? done
- Add a CLI and/or REST API (using, eg, FastAPI) to interact with your library. 
- Containerize your app in Docker.
- Whatever else you'd like.