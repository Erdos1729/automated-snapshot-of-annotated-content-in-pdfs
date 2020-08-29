## Automated snapshot of annotated content in pdfs
 This repository will automate the process of saving snapshots of highlighted content within multiple pdf files.

## Instructions

-   pip install -r requirements
-   Run snapshot_ext.py

## Reference

I composed the solution out of the following pages of the documentation:

[![Tutorial](https://pymupdf.readthedocs.io/en/latest/tutorial/)] page to get introduced into the library
[![page.searchFor](https://pymupdf.readthedocs.io/en/latest/page/#Page.searchFor)] to figure out the return type of the searchFor method
[![fitz.Rect](https://pymupdf.readthedocs.io/en/latest/rect/#rect)] to understand what the returned objects from page.searchFor are
[![Collection of Recipes](https://pymupdf.readthedocs.io/en/latest/faq/)] page (called faq in the URL) to figure out how to crop and save part of a pdf page

## 🚀 Quickstart

Installing the requirements will automatically install all dependencies. Make sure you install the requirements
before running the code. Also note that this requires **Python 3.6+**.