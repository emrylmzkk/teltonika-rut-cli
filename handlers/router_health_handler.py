from rich.console import Console
from services.router_health_service import RouterHealthService

console = Console()

def handle_check_router():

    console.print("\n[yellow]Checking router connectivity...[/yellow]\n")
    
    router_service = RouterHealthService()
    
    result = router_service.check_router_health()


    console.print(
        f"Ping   : {'[green]✔ reachable[/green]' if result['ping'] else '[red]✘ failed[/red]'}"
    )

    console.print(
        f"SSH    : {'[green]✔ open[/green]' if result['ssh'] else '[red]✘ closed[/red]'}"
    )

    console.print(
        f"HTTP   : {'[green]✔ open[/green]' if result['http'] else '[red]✘ closed[/red]'}"
    )

    console.print(
        f"HTTPS  : {'[green]✔ open[/green]' if result['https'] else '[red]✘ closed[/red]'}"
    )

          
        
