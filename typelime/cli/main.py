from typer import Typer

from typelime.cli.ops import op_app
from typelime.cli.mappers import map_app

main_app = Typer(
    invoke_without_command=False,
    pretty_exceptions_enable=False,
    add_completion=False,
    no_args_is_help=True,
)
main_app.add_typer(op_app)
main_app.add_typer(map_app)


def main() -> None:
    main_app()


if __name__ == "__main__":
    main()