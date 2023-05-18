\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{poster}[2017/11/27 class to DCM/FFCLRP/USP graduate manuscript template]

% --- Class structure: declaration of options part
% ---
% This class extends the a0poster class
% Read all the documentclass options; pass them to a0poster,
% unless the file "<currentoption>.ppgcaposter" exists, then it is loaded
\DeclareOption*{\InputIfFileExists{\CurrentOption.poster}{}{
    % 
    \PassOptionsToClass{\CurrentOption}{a0poster}}}

% --- Class structure: execution of options part
% ---
\ProcessOptions \relax
% --- Class structure: declaration of options part
% ---
\LoadClass{a0poster}

\ExecuteOptions{final}
\ProcessOptions
% PACKAGES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{fontspec}
\RequirePackage{multicol} % This is so we can have multiple columns of text side-by-side
\columnsep=100pt % This is the amount of white space between the columns in the poster
\columnseprule=3pt % This is the thickness of the black line between the columns in the poster
\RequirePackage{babel}
\RequirePackage{babelbib}

\RequirePackage[svgnames]{xcolor} 
\RequirePackage{amsmath}
\RequirePackage{graphicx} % Required for including images
\RequirePackage{booktabs} % Top and bottom rules for table
\RequirePackage[font=small,labelfont=bf]{caption} % Required for specifying captions to tables and figures
\RequirePackage{amsfonts, amsmath, amsthm, amssymb} % For math fonts, symbols and environments
\RequirePackage{wrapfig} % Allows wrapping text around tables and figures
\RequirePackage{tikz}
\usetikzlibrary{calc}
\usetikzlibrary{fadings}
\RequirePackage{caption}
\RequirePackage{etoolbox}
\DeclareGraphicsRule{.ai}{pdf}{.ai}{}
\RequirePackage{lipsum}  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% FONTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% size 24.88pt


% \renewcommand{\tiny}{\fontsize{18}{21}\selectfont}
% \renewcommand{\scriptsize}{\fontsize{21.6}{27}\selectfont}
% \renewcommand{\footnotesize}{\fontsize{25.92}{33}\selectfont}
% \renewcommand{\small}{\fontsize{31.01}{37.5}\selectfont}
% \renewcommand{\normalsize}{\fontsize{37.32}{45}\selectfont}
% \renewcommand{\large}{\fontsize{44.79}{55.5}\selectfont}
% \renewcommand{\Large}{\fontsize{53.745}{67.5}\selectfont}
% \renewcommand{\LARGE}{\fontsize{64.5}{81}\selectfont}
% \renewcommand{\huge}{\fontsize{77.4}{96}\selectfont}
% \renewcommand{\Huge}{\fontsize{92.88}{115.5}\selectfont}
% \renewcommand{\veryHuge}{\fontsize{111.45}{139.5}\selectfont}
% \renewcommand{\VeryHuge}{\fontsize{133.74}{168}\selectfont}
% \renewcommand{\VERYHuge}{\fontsize{160.5}{201}\selectfont}

\renewcommand{\tiny}{\fontsize{24}{28}\selectfont}
\renewcommand{\scriptsize}{\fontsize{28.8}{36}\selectfont}
\renewcommand{\footnotesize}{\fontsize{34.56}{44}\selectfont}
\renewcommand{\small}{\fontsize{41.48}{50}\selectfont}
\renewcommand{\normalsize}{\fontsize{47.76}{60}\selectfont}
\renewcommand{\large}{\fontsize{55}{70}\selectfont}
\renewcommand{\Large}{\fontsize{71.66}{90}\selectfont}
\renewcommand{\LARGE}{\fontsize{85}{108}\selectfont}
\renewcommand{\huge}{\fontsize{103.2}{128}\selectfont}
\renewcommand{\Huge}{\fontsize{123.84}{154}\selectfont}
\renewcommand{\veryHuge}{\fontsize{148.6}{186}\selectfont}
\renewcommand{\VeryHuge}{\fontsize{178.32}{224}\selectfont}
\renewcommand{\VERYHuge}{\fontsize{214}{268}\selectfont}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MARGINS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% A0 dimensions 841 x 1189 mm  33.1 x 46.8 in
\special{papersize=46.8in,33.1in}
\setlength{\paperwidth}{84.1cm}
\setlength{\paperheight}{118.9cm}
\setlength{\textwidth}{80.1cm}
\setlength{\textheight}{114.9cm}

\topskip0pt
\setlength{\headheight}{0pt}
\setlength{\headsep}{0pt}
\setlength{\topmargin}{0pt}
\setlength{\oddsidemargin}{0pt}

\setlength{\oddsidemargin}{2cm}

\newcommand\printheader{
\begin{minipage}[ht]{0.1\linewidth}
  % \includegraphics[trim={0 15cm 0 0}, clip, scale=.25]{HYlogo.png}
\end{minipage}\vspace{0.5cm}
}