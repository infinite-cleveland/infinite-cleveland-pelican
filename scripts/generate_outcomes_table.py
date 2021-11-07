import json
import os


"""
generate_outcomes_table.py

This script uses data in ../data/outcomes.json
to generate a table of outcomes in ../pelican/content/index.html
"""


dry_run = False

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA = os.path.join(ROOT, 'data')
PELICANCONTENT = os.path.join(ROOT, 'pelican', 'content')


index_html_file = os.path.join(PELICANCONTENT, 'index.html')
print(f"Loading existing index.html file from {index_html_file}")
with open(index_html_file, 'r') as f:
    index_html = f.readlines()

# Preserve content before/after table
new_index_html_top = []
for line in index_html:
    if "BEGIN INFINITE CLEVELAND TABLE" in line:
        new_index_html_top.append(line)
        break
    else:
        new_index_html_top.append(line)

new_index_html_bot = []
reached = False
for line in index_html:
    if "END INFINITE CLEVELAND TABLE" in line:
        reached = True
        new_index_html_bot.append(line)
    elif reached:
        new_index_html_bot.append(line)

# Assemble the actual table
table_head = """
        <table class="table" style="text-align: center; border: 1px solid black;">
            <thead>
                <tr>
                    <th width="150">Game</th>
                    <th>Winnner</th>
                    <th width="150">Score</th>
                    <th>Loser</th>
                    <th width="150">Innings</th>
                    <th width="300">Links</th>
                </tr>
            </thead>
            <tbody>
"""

table_tail = """
            </tbody>
        </table>
"""

table_row_template = """
                <tr>
                    <td>
                        <a href="#">Game {game_index}</a>
                    </td>
                    <td style="background-color: #{winner_color}; color: #eee; font-weight: bold;">{winner_name}</td>
                    <td>{winner_runs}-{loser_runs}</td>
                    <td style="background-color: #{loser_color}; color: #eee;">{loser_name}</td>
                    <td>({innings})</td>
                    <td>
                        <button type="button" class="btn btn-small btn-secondary">Box Score</button>
                        <button type="button" class="btn btn-small btn-secondary">Play By Play</button>
                    </td>
                </tr>
"""

outcomes_json_file = os.path.join(DATA, 'outcomes.json')
if not os.path.exists(outcomes_json_file):
    raise Exception(f"Error: could not find outcomes.json file {outcomes_json_file}")
with open(outcomes_json_file, 'r') as f:
    outcomes_json = json.load(f)

new_index_html_table = []

new_index_html_table.append(table_head)

for outcome in outcomes_json:
    table_row = table_row_template.format(
        game_index=outcome['Index']+1,
        winner_name=outcome['WName'],
        winner_color=outcome['WColor'],
        winner_runs=outcome['WRuns'],
        loser_name=outcome['LName'],
        loser_color=outcome['LColor'],
        loser_runs=outcome['LRuns'],
        innings=outcome['Innings'],
    )
    new_index_html_table.append(table_row)

new_index_html_table.append(table_tail)

# Assemble the final index.html file
page_text = ""
page_text += "".join(new_index_html_top)
page_text += "\n".join(new_index_html_table)
page_text += "".join(new_index_html_bot)

if dry_run:
    print('-----------------------------------')
    print(page_text)
else:
    print(f"Writing new index.html file to {index_html_file}")
    with open(index_html_file, 'w') as f:
        f.write(page_text)

