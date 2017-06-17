import argparse
import random

# Argument parsing
parser = argparse.ArgumentParser(description='Calculates the entropy of a file.')
parser.add_argument('Size',
                    help='The size, in bytes, to simulate a malware file.',
                    type=int)
parser.add_argument("-w", "--window",
                    help="Window size, in bytes, for running entropy."
                         "", type=int, required=True)
parser.add_argument("-s", "--seed",
                    help="The seed value to the random function to simulate a malware file."
                         "", default=0, type=int, required=False)

args = parser.parse_args()

k = args.Size
j = args.window

# Create a random file, based upon seed, for the simulated malware file.
random.seed(args.seed)
malware = [random.randint(0, 7) for i in range(1, k+1)]

print("malware")
print(malware)

for x in range(1, k-j+2):
    m = [0 for i in range(0, 8)]
    for y in range(1, j+1):
        m[malware[x+y-2]] += 1
