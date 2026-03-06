from rich.console import Console
from rich.panel import Panel
from services.connection.router_rest_client import RouterRestClient
from handlers.relay_handler import handle_relay_reboot


console = Console()

def main():

    client = RouterRestClient()

    console.print(
        Panel.fit(
            "[bold green]TELTONIKA CLI[bold green]",
            border_style="green"
        )
    )

    console.print("\n[bold]Menu:\n")

    console.print("1-) Relay Reboot (3 seconds)")
    console.print("q-) Exit")

    user_choice = console.input("\n[bold red]Select Option > [/bold red]")

    console.print(f"\n Selected option : [bold]{user_choice}[bold]")

    match user_choice:

        case "1":
            handle_relay_reboot()

        case "q":
            console.print("[bold red]Exiting...[/bold red]")
            
        case _:
            console.print("[red] Invalid option[/red]")
            
if __name__ == "__main__":
    main()