import subprocess
import threading
import time
import click

@click.command()
@click.option('--message', prompt='Enter the message', help='The message you want to send')
@click.option('--numbers-file', prompt='Enter the numbers file name', help='The file containing phone numbers')
@click.option('--delay', type=float, prompt='Enter the delay in seconds', help='The delay between sending messages')
def main(message, numbers_file, delay):
    numbers = load_numbers(numbers_file)
    if not numbers:
        click.echo(f"No numbers found in {numbers_file}. Aborting.")
        return
    
    click.echo(f"Starting SMS sending with the following parameters:")
    click.echo(f"Message: {message}")
    click.echo(f"Numbers file: {numbers_file}")
    click.echo(f"Delay: {delay} seconds")
    click.confirm("Do you want to proceed?", abort=True)

    click.echo("Sending SMS messages...")
    click.echo("Press Ctrl+C to stop.")
    click.echo("-------------------------------------")
    
    for number in numbers:
        threading.Thread(target=send_sms, args=(number, message)).start()
        time.sleep(delay)

def load_numbers(numbers_file):
    try:
        with open(numbers_file) as f:
            numbers = [line.strip() for line in f]
        return [f'+1{number}' for number in numbers]
    except FileNotFoundError:
        return []

def send_sms(number, message):
    cmd = f"termux-sms-send -n {number} '{message}'"
    try:
        subprocess.run(cmd, shell=True, check=True)
        click.echo(f"Message sent to {number}")
    except subprocess.CalledProcessError:
        click.echo(f"Failed to send message to {number}")

if __name__ == "__main__":
    main()
