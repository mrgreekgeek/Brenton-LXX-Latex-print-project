import re,sys

HEAD = r"""\input{preamble.tex}

\title{Η ΠΑΛΑΙΑ ΔΙΑΘΗΚΗ}
\author{Ἡ μετάφρασις τῶν Ἑβδομήκοντα}
\date{}

\begin{document}
\begin{spacing}{1.1}
\maketitle

\tableofcontents

\begin{multicols}{2}
"""

FOOT = r"""\end{multicols} % End two-column layout
\vfill
\setlength{\parindent}{0cm}
\fontsize{8}{10}\selectfont{This work is in the public domain. \\The text source is available at: \underline{https://ebible.org/Scriptures/details.php?id=grcbrent}. \\This PDF file created by MrGreekGeek, available from \underline{https://github.com/mrgreekgeek/Brenton-LXX-Latex-print-project}.}

\end{spacing}
\end{document}"""

with open(sys.argv[1], "r", encoding="utf-8") as input:
    with open(sys.argv[2], "w", encoding="utf-8") as output:           
        latex = input.read()

        # Fix typos/issues in the source text
        latex = re.sub(r',,', r',', latex, flags=re.M)              # Exodus 33:13
        latex = re.sub(r'ʼΑλλʼ', r'Ἀλλ’', latex, flags=re.M)        # Psalm 1:2
        latex = re.sub(r'(\\par \}\{\\PP )(Ὁ Θεὸς ἔστη ἐν συναγωγῇ θεῶν,)', r'\1\\VS{2}\2', latex, flags=re.M) # Fix missing verse number from Psalm 81:2
        latex = re.sub(r'(\\par \}\{\\PP )(Κλίνον Κύριε τὸ οὖς σου,)', r'\1\\VS{2}\2', latex, flags=re.M) # Fix missing verse number from Psalm 85:2
        latex = re.sub(r'\n\\VS\{2\}(ὁπότε ἐνεπύρισε .*?\.)', r' \1', latex) # Remove verse number from Psalm 59 header

        # Set up chapter names and multi-columns
        latex = re.sub(r'\{\\MT (.*)', r'\\end{multicols}\n\\def\\book{\1}\n\\biblebook{\1}\n\\begin{multicols}{2}', latex, flags=re.M)

        latex = re.sub(r'ChapOne\{1\}', r'ch{1}', latex, flags=re.M)
        latex = re.sub(r'OneChap', r'ch{1}', latex, flags=re.M)
        latex = re.sub(r'\\VerseOne\{2a\}', r'', latex, flags=re.M)

        # Clean up xetex formatting
        latex = re.sub(r'\\NormalFont\\ShortTitle\{.*?\}', r'', latex, flags=re.M)
        latex = re.sub(r'﻿', r'', latex, flags=re.M)
        latex = re.sub(r'\. [Α-Ωϛ]+ʹ', r'', latex, flags=re.M)
        latex = re.sub(r'^\\par }', r'', latex, flags=re.M)
        latex = re.sub(r'\{\\MM ', r'', latex, flags=re.M)
        latex = re.sub(r'\{\\IP ', r'', latex, flags=re.M)
        latex = re.sub(r'\{\\IS ', r'', latex, flags=re.M)
        latex = re.sub(r'\{\\SH ', r'', latex, flags=re.M)

        # Psalm headings
        latex = re.sub(r'\\PsalmChap\{(\d+)\}\{\\D \\VerseOne\{1\}(.*)\n', r'\\psalmheading{\\ch{\1} \2}', latex, flags=re.M)
        latex = re.sub(r'\\PsalmChap\{(\d+)\}\{\\PP \\VerseOne\{1\}', r'\\ch{\1} ', latex, flags=re.M)
        
        # Note at the end of Psalm 71
        latex = re.sub(r'\{\\D \\VS\{20\}(.*)', r'\n\\textit{\1}', latex, flags=re.M)
        
        latex = re.sub(r'\\Chap\{(\d+)\}', r'\\ch{\1}', latex, flags=re.M)
        latex = re.sub(r'\\VerseOne\{1\}', r'', latex, flags=re.M)
        latex = re.sub(r'VS(\{\d+|\d+[a-z]\})', r'vs\1', latex, flags=re.M)
        latex = re.sub(r'\{\\PP ', r'\n', latex, flags=re.M)

        # Keep psalm headings together with next verse
        latex = re.sub(r'\\psalmheading(\{\\ch\{\d+\}.*?\})(\n|)(.*?\n)', r'\\begin{psalmhead}\1\2\3\\end{psalmhead}\n', latex, flags=re.M)

        output.write(HEAD + latex + FOOT)