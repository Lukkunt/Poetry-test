import click


@click.command()
@click.argument("name")
@click.option("--number", type=int, help="Help message for int here")
def main(name, number):
    """
    Help message
    """
    for i in range(number):
        print(f"Hello {name}!")


if __name__ == "__main__":
    main()
