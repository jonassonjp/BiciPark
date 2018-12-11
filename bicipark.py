#!/usr/bin/env python3
# bicipark.py
import sys


def main(argv):
    if argv is None:
        argv = sys.argv
    print("Rodando o sistema com os argumentos: {}".format(argv))


if __name__ == "__main__":
    main(sys.argv)

