from random_dict import gen_func_QA3, gen_func_multi_bg, gen_func  

def loop(suffix, amount):
  print(f"suffix = {suffix}, amount = {amount}")
  for i in range(amount):
    final_url = gen_func(f"{suffix}_{i}")
    return final_url

