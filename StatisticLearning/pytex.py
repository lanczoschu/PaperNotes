from pylatex import Document, Section, Subsection, Command, Tabularx, Tabular, Figure, Package, Center, FlushLeft, Itemize
from pylatex.utils import NoEscape, escape_latex
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots
plt.style.use(['science', 'nature'])

def clean_pandas(df, round=3, sub_indexes=None, sub_columns=None, del_indexes=None, del_columns=None):
    if sub_indexes is not None:
        sub_rows = []
        for one_kind_index in sub_indexes:
            sub_rows += [i for i in tuple(df.index) if one_kind_index in i]
        df = df.loc[sub_rows]

    if sub_columns is not None:
        sub_cols = []
        for one_kind_column in sub_columns:
            sub_cols += [i for i in tuple(df.columns) if one_kind_column in i]
        df = df[sub_cols]
    
    if del_indexes is not None:
        df = df.rename(index={i:del_indexes(i) for i in df.index})
    if del_columns is not None:
        df = df.rename(columns={i:del_columns(i) for i in df.columns})

        # df = 
    return df.round(round)

class MyDocument(Document):
    def __init__(self, title, documentclass='poster', document_options='portrait', font_size='large'):
        super().__init__(documentclass=documentclass, document_options=document_options, font_size=font_size)

        self.packages.append(Package('hyperref'))
        self.packages.append(Package('float'))
        self.packages.append(Package('epigrafica'))
        self.packages.append(Package('fontenc', options=['LGR', 'OT1']))
        self.packages.append(Package('graphicx'))
        # self.packages.append(Package('epstopdf'))

        self.preamble.append(Command('title', title))
        self.preamble.append(Command('author', 'Jiajun Zhu'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        
        self.append(NoEscape(r'\maketitle'))
        self.append(NoEscape(r'\printheader'))
        # self.append(Command('setmainfont', 'Calibri'))


    def create_csv2tab(self, csv_file, table_index, caption, notes='', sub_indexes=None, del_indexes=None, sub_columns=None, del_columns=None, avg_std=False):
        data = pd.read_csv(csv_file, index_col=0)
        data = clean_pandas(data, round=3, sub_indexes=sub_indexes, sub_columns=sub_columns, del_indexes=del_indexes, del_columns=del_columns)
        with self.create(Center()) as table:
            self.append(NoEscape(("\captionof{table}{%s}") % (caption)))
            if not avg_std:
                with table.create(Tabular('l'+'c'*(len(data.columns)-1)+'r', booktabs=True, col_space='1cm')) as tabular:
                    # doc.append(NoEscape(r'\toprule'))
                    tabular.add_row((table_index, )+tuple(data.columns))
                    tabular.append(NoEscape(r'\midrule'))
                    [tabular.add_row((data.iloc[i].name, )+tuple(data.iloc[i])) for i in range(len(data))]
            else:
                avg_cols = [avg_col for avg_col in data.columns if 'avg' in avg_col]
                std_cols = [avg_col.replace('avg', 'std') for avg_col in avg_cols]
                avg_data = data[avg_cols].applymap(str)
                std_data = data[std_cols].applymap(str)
                new_data = avg_data.str.cat(std_data, sep='\pm')
                with table.create(Tabular('l'+'c'*(len(avg_data.columns)-1)+'r', booktabs=True, col_space='1cm')) as tabular:
                    # doc.append(NoEscape(r'\toprule'))
                    tabular.add_row([table_index] + [i.replace('_avg', '') for i in avg_data.columns])
                    tabular.append(NoEscape(r'\midrule'))
                    [tabular.add_row((data.iloc[i].name, )+tuple(data.iloc[i])) for i in range(len(data))]
            # table.append(NoEscape(r'\bottomrule'))
            # with doc.create(Center()) as c:
            
            if notes:
                self.append(Command('vspace', '0.3cm'))
                with self.create(FlushLeft()) as c:
                    c.data += [NoEscape(r"\footnotesize~")] + [escape_latex(note) for note in notes]
            
        # self.append(Command('vspace', '1cm'))

    def create_plt2fig(self, width, *args, **kwargs):
        with doc.create(Figure(position='H')) as plot:
            plot.add_plot(width=NoEscape(f'{width}\\textwidth'), return_path='fig1.eps', *args, **kwargs)
            plot.add_caption('I am a caption.')
            plot.append(Command('label', 'Fig:1'))

if __name__ == '__main__':
    

    # Document
    doc = MyDocument('Explanation Variation Exp', font_size='large')
    # Call function to add text
    doc.append(Command('begin', arguments=['multicols', 2]))
    
    fp = open("./observation.txt")
    texts = ''.join(fp.read().splitlines())
    # texts = "Recently some articles the uncertainty of the explanation like \href{https://arxiv.org/abs/1910.12336}{CXPlain}. These works gave a natural question: whether the most important nodes have lower uncertainty."
    with doc.create(Section('Idea | Observation', numbering=False)):
        doc.append(NoEscape(texts))
    
    f = open("./method.txt")
    with doc.create(Section('Methods & Setting', numbering=False)):
        with doc.create(Itemize()) as itemize:
            for line in f.read().splitlines():
                itemize.add_item(NoEscape(line))

    des = '''Table 1 shows the Spearman Correlation between avg/std IMP scores on x nodes. Except for classifier 1/3/5 
which fails to provide high explanation auc (see Table 2), i.e. cannot distinguish signal nodes and bkg nodes, others' coef 
on all nodes are negative. And the coef on signal nodes are all -1.'''

    r_txt = open("./result.txt")
    res = ''.join(r_txt.read().splitlines())
    with doc.create(Section('Experiment Results', numbering=False)):
        table_notes = ["i) seed refers to different classifiers trained with different seeds; ",
            "ii) x_nodes means we only compute the spearman correlation of avg/std IMP on x_nodes."]
        csv_file = r'D:\Projects\REPOS\Renaissance\src\result\egnn_synmol\uncertainty\pgexplainer.csv'

        doc.append(NoEscape(des))
        
        doc.create_csv2tab(csv_file, table_index='seed', caption='Spearman Correlation of avg/std node IMP', notes=None,
                        del_indexes=lambda x: x[5], sub_columns=['spearman'], del_columns=lambda x: x.replace('spearman', 'nodes'))

        doc.append(NoEscape(res))
        doc.create_csv2tab(csv_file, table_index='seed', caption='Explanation AUC of avg/-std node IMP', del_indexes=lambda x: x[5], sub_columns=['exp_auc', 'acc'])
    
        # doc.append(NoEscape(r"\newpage"))

        # with doc.create(Subsection('Analysis', numbering=False)):
        
    # x = [0, 1, 2, 3, 4, 5, 6]
    # y = [15, 2, 7, 1, 5, 6, 9]
    # plt.plot(x, y)
    # doc.create_plt2fig(width=0.5, dpi=300)
    # plt.savefig('test.eps', dpi=300, bbox_inches='tight', pad_inches=0, transparent=True)
    
    # Add stuff to the document


    doc.append(Command('end', arguments=['multicols']))
    doc.generate_pdf('Stability', compiler='xelatex', clean_tex=False)
    # tex = doc.dumps()  # The document as string in LaTeX syntax


