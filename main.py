from rich.console import Console
from rich.panel import Panel
from services.connection.router_rest_client import RouterRestClient
from handlers.relay_handler import handle_relay_reboot
from handlers.router_health_handler import handle_check_router
from handlers.router_general_handler import handle_get_firmware


console = Console()

def main():

        console.print(
        Panel.fit(
            "[bold green]TELTONIKA CLI[bold green]",
            border_style="green"
            )
        )

        console.print("\n[bold]Menu:\n")

        
        console.print("1-) Check Router")
        console.print("2-) Check Router Information")
        console.print("3-) Relay Reboot (3 seconds)")
        console.print("q-) Exit")
        
        console.print("[bold green]\n-----------------------------------\n[bold green]")

        while True:

            user_choice = console.input("\n[bold red]Select Option > [/bold red]")

            console.print(f"\n Selected option : [bold]{user_choice}[bold]")

            match user_choice:

                

                case "1":
                    handle_check_router()

                case "2":
                      handle_get_firmware()

                case "3":
                    handle_relay_reboot()


                case "Q" | "q":
                    console.print("[bold red]Exiting application...[/bold red]")
                    break

                case _:
                    console.print("[red] Invalid option[/red]")
            
if __name__ == "__main__":
    main()