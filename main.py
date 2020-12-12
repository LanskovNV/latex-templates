import jinja2
import os


def create_latex_env():
    latex_jinja_env = jinja2.Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    return latex_jinja_env


def save_rendered_template(template, fname):
    header_pattern = '| c | c || c | c |'
    header = ['Вариант', 'Пересечение', 'Вариант', 'Пересечение']
    data = [
        [1, 'WN, NS', 9, 'SN, WE'],
        [2, 'WN, NE', 10, 'SN, EW'],
        [3, 'WN, SW', 11, 'SN, ES'],
        [4, 'WN, EW', 12, 'NE, EW'],
        [5, 'NS, SW', 13, 'NE, ES'],
        [6, 'NS, WE', 14, 'SW, WE'],
        [7, 'NS, EW', 15, 'SW, ES'],
        [8, 'SN, NE', 16, 'WE, ES'],
    ]
    with open(fname, 'w') as res:
        res.write(template.render(header_pattern=header_pattern, header=header, data=data))


if __name__ == '__main__':
    env = create_latex_env()
    template_name = 'templates/table1.tex'
    render_name = 'output/res.tex'

    template = env.get_template(template_name)

    save_rendered_template(template, render_name)
