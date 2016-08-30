import argparse
import re
import json



parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("-f", "--file",type=str)
parser.add_argument("-n", "--node",type=int, help="node number")
args = parser.parse_args()


with open(args.file) as data_file:    
    data = json.load(data_file)


print("# FT Settings for Node %d" % args.node)
print("nas_identifier=node%s.snc.int" % args.node)
print("r1_key_holder=00deadbeef%02x" % args.node)
print("mobility_domain=%s" % data["mobility_domain"])
print("pmk_r1_push=%d" % data["pmk_r1_push"])

# r0kh generation
for i in data["nodes"]:
    print("r0kh=%s %s%s.%s %s" %(
        data["nodes"][i]["mac"],
        data["nas_id_prefix"],
        i,
        data["nas_id_suffix"],
        data["nodes"][i]["key"]
    ))

    print("r1kh=%s 00:de:ad:be:ef:%02x %s" %(
        data["nodes"][i]["mac"],
        int(i),
        data["nodes"][str(args.node)]["key"]
    ))
