import matplotlib.pyplot as plt
import scienceplots
import contextlib
import sys
from tably import csv2tex
from datetime import datetime


plt.style.use(['science', 'nature'])

tex_header = '''\\documentclass{article}\n
            \\usepackage{graphicx}\n
            \\usepackage{caption, subcaption}\n
            \\begin{document}\n'''

def fig2tex(file, fig_path, wid=0.8, notes=''):
    # linewidth, textwidth, columnwidth
    tex_content = r'''\begin{figure}[htbp]
                    \centering
                    \includegraphics[width=%f\textwidth]{%s} 
                        \begin{center}
                        \footnotesize %s
                        \end{center}
                    \caption{something}\label{fig:1}
                    \end{figure}''' % (wid, fig_path, notes)
    return file.write(tex_content)


Exp_ID = datetime.now().strftime("%m-%d-%H")
table_dir = r"C:\Users\86173\Desktop\0503\inherent\lri_bern_lri_gaussian_vgib_ciga_egnn_synmol.csv"
fig_dir = f'test'
Latex_file = open(f'{Exp_ID}.tex', 'w+')
Latex_file.write(tex_header)
# write table
with contextlib.redirect_stdout(Latex_file):
    csv2tex([table_dir])



# include figure
fig2tex(Latex_file, fig_dir, notes='')
