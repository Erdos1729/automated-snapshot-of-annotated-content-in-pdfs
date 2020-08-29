## Automated snapshot of annotated content in pdfs
 This repository will automate the process of saving snapshots of highlighted content within multiple pdf files.

## Instructions

-   pip install -r requirements
-   Run snapshot_ext.py

## Reference

I composed the solution out of the following pages of the documentation:

-   [![Tutorial](https://pymupdf.readthedocs.io/en/latest/tutorial/)] page for introduction to the fitz liabrary
-   [![page.searchFor](https://pymupdf.readthedocs.io/en/latest/page/#Page.searchFor)] to solve the return type for searchFor method
-   [![fitz.Rect](https://pymupdf.readthedocs.io/en/latest/rect/#rect)] to identify what the returned objects from page.searchFor
-   [![Collection of Recipes](https://pymupdf.readthedocs.io/en/latest/faq/)] page (called faq in the URL) to implement cropping and saving part of a pdf page

## 🚀 Quickstart

Installing the requirements will automatically install all dependencies. Make sure you install the requirements
before running the code. Also note that this requires **Python 3.6+**.