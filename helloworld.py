import sys

def main():
    print("Hello World! From Phyton: " + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # let's make this script fail for Phyton 3.6
        raise Exception('Phyton version 3.6.x is unsupported!')

if __name__ == "__main__":
    main()
