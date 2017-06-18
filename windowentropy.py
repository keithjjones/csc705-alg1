import argparse
import random
import math
import time


# Window Entropy Function
def window_entropy():
    # Compute the running entropy
    for x in range(1, k - j + 2):
        m = [0 for i in range(0, 256)]
        for y in range(1, j + 1):
            m[malware[x + y - 2]] += 1
        entropy = float(0)
        for y in range(0, 256):
            if m[y] != 0:
                entropy += -(float(m[y] / j) * math.log2(float(m[y] / j)))
        H[x - 1] = entropy / K

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
parser.add_argument("-K", "--K",
                    help="The K scale value. Must not be zero."
                         "", default=1, type=int, required=False)
parser.add_argument("-a", "--average",
                    help="The number of runs for averaging, greater than zero."
                         "", default=1, type=int, required=False)

args = parser.parse_args()

k = args.Size
j = args.window
K = args.K

# Create a random file, based upon seed, for the simulated malware file.
random.seed(args.seed)
malware = [random.randint(0, 255) for i in range(1, k+1)]
# print("Malware: {0}".format(malware))

totaltime = 0

for a in range(0, args.average):
    # Start the time counter
    starttime = time.process_time()

    # Entropy list
    H = [0 for i in range(1, k-j+2)]

    # Calculate the window entropy
    window_entropy()

    endtime = time.process_time()
    totaltime += endtime - starttime

# print("Entropy: {0}".format(H))
print("Average Running Time for {1} Iterations: {0:.4E}".format(totaltime/args.average, args.average))