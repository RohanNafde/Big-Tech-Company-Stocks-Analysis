(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt" "twocolumn")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("ragged2e" "document")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "graphicx"
    "enumitem"
    "kantlipsum"
    "ragged2e"
    "hyperref"
    "geometry"
    "titlesec"
    "floatrow"
    "caption"
    "sectsty")
   (LaTeX-add-labels
    "sec:intro"
    "sec:eda"))
 :latex)

