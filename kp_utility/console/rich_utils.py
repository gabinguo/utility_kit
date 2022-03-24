from rich.console import Console, Group
from rich import box
from rich.table import Table
from rich.panel import Panel

from typing import List

console = Console()
# rich configs
rich_colors = ["dodger_blue1", "spring_green3", "blue_violet", "medium_violet_red", "gold3", "yellow3", "salmon1"]
rich_table_title_style = "bold spring_green3 on salmon1"


def generate_stats_rich_table(title: str, columns: List[str], rows: List[List[str]], h_style: str = "salmon1",
                              v_style: str = "bold spring_green1"):
    table = Table(title=title, title_style=rich_table_title_style, expand=True, show_header=True,
                  box=box.SIMPLE_HEAVY, header_style="bold spring_green3")
    table.add_column(header=columns[0].capitalize(), justify="left", style=v_style)
    for column in columns[1:]:
        table.add_column(header=column.capitalize(), justify="center", style=h_style)
    for row in rows:
        table.add_row(*row)
    return table


def display_panel_with_tables(tables, title="Panel"):
    group = Group(*tables)
    console.print("\n")
    console.print(Panel(group, title=title, padding=1, box=box.DOUBLE_EDGE, expand=True))
    console.print("\n")


def test_example():
    table_ = generate_stats_rich_table("Table 1", ["", "A", "B"], [["C", "C", "C"]])
    display_panel_with_tables([table_], "Panel 1")


if __name__ == '__main__':
    test_example()
