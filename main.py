from openseatrader import wrapper

meta = wrapper.retrieve_a_single_collection("crypto-coral-tribe")
print(meta.json_data)
