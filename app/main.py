import subprocess
import sys

def main():
    # Extract the command and arguments from the command line arguments
    command = sys.argv[3]
    args = sys.argv[4:]

    # Create a subprocess that connects the stdout and stderr to the respective streams of the parent process
    completed_process = subprocess.Popen(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Communicate with the process to read the stdout and stderr, then write it to the parent process' streams
    stdout, stderr = completed_process.communicate()
    sys.stdout.buffer.write(stdout)
    sys.stdout.buffer.flush()
    sys.stderr.buffer.write(stderr)
    sys.stderr.buffer.flush()

if __name__ == "__main__":
    main()
