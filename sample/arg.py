# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--name", "-n", help="set output name")
parser.add_argument("--email", "-e", help="set output email")

# read arguments from the command line
args = parser.parse_args()

# check for --name, --email
if args.name:
    print("set output name to %s" % args.name)

if args.email:
    print("set output email to %s" % args.email)

print("My name is {}. email: {}".format(args.name, args.email))