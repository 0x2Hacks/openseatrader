import openseatrader as ot

meta = ot.retrieve_a_single_collection("crypto-coral-tribe")
print(meta.json_data)
