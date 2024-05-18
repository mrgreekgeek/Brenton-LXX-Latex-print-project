# Brenton's Septuagint in Latex

This repository's purpose is to make Brenton's Septuagint available in print-ready format for free. If you do a search for printed Septuagint Bibles online, you will quickly find that they are very large and heavy and quite expensive. We want to change that! This edition is designed to be as compact as possible, and the price can't be beat. :) 

## Details
**Brenton.pdf**  
The main files in this repo are `Brenton.tex` and `Brenton.pdf`. If you want to print a book of your own, just download the latest release of [Brenton.pdf](https://github.com/mrgreekgeek/Brenton-LXX-Latex-print-project/releases/latest/download/Brenton.pdf) and send it to your local print shop or your favorite self-publishing company. I have used [Snowfall Press](https://www.snowfallpress.com/) with good results. (Choose their lightest paper, "White, 40# / 13LB Bond" as that will help keep the size and weight of the book down.)

**Process.py**  
`Process.py` is the main worker. It takes the concatenated xetex files (see below) and transforms them into `Brenton.tex`, which is the source for `Brenton.pdf`. If you want to modify the PDF in any way, you'll need to modify `Brenton.tex` and then run it through LaTex to create a new PDF file. This repo uses LuaLaTex via [MikTex](https://miktex.org/).  

## Source and License
The digital Brenton LXX text is sourced from [ebible.org](https://ebible.org/Scriptures/details.php?id=grcbrent) and is in the public domain. (The exact source for the files in `grcbrent_xetex` is the [ebible XeTeX file](https://ebible.org/Scriptures/grcbrent_xetex.zip). You can use the script `concat.py` to merge each individual book into one file (concatenated.tex) as we did here.) All of the code and `.tex` formatting are licensed [CC0-1.0 (public domain)](https://github.com/mrgreekgeek/Brenton-LXX-Latex-print-project/blob/main/LICENSE) and may be used and copied freely. May God get all the glory! 

## TODO 
- [x] Add book names to the running header
- [x] Add chapter:verse references to the running header like most Bibles have 
- [x] Keep all Psalm headings with the following paragraphs
- [ ] Add front matter (copyright, editor, year, etc)