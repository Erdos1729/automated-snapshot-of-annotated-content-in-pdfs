## Automated snapshot of annotated content in pdfs
 This repository will automate the process of saving snapshots of highlighted content within multiple pdf files.

## Instructions

-   pip install -r requirements
-   Run snapshot_ext.py

## Reference

I devised the solution from the following pages of the documentation:

-   [Tutorial(https://pymupdf.readthedocs.io/en/latest/tutorial.html) page for introduction to the fitz liabrary
-   [page.searchFor](https://pymupdf.readthedocs.io/en/latest/page.html)to solve the return type for searchFor method
-   [fitz.Rect](https://pymupdf.readthedocs.io/en/latest/rect.html) to identify what the returned objects from page.searchFor
-   [fitz.Point](https://pymupdf.readthedocs.io/en/latest/functions.html) to provide parameters to create a cropping box around the highlighted content
-   [Collection of Recipes](https://pymupdf.readthedocs.io/en/latest/faq.html) page to implement cropping, saving and working with images as spnapshots

## 🚀 Quickstart

Installing the requirements will automatically install all dependencies. Make sure you install the requirements
before running the code. Also note that this requires **Python 3.6+**.