import json


jobj = {"wolf_b":"beta","wolf_a":"alpha"}
dump_str = json.dumps(jobj, indent=4)
# the indent option helps pretty print json by indenting the output by
# the number of space specified

print(dump_str)
# OUTPUT:
# {
#     "wolf_b": "beta",
#     "wolf_a": "alpha"
# }


