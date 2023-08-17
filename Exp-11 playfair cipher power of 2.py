import math
def num_possible_keys():
  """Calculates the number of possible keys for the Playfair cipher."""
  return math.pow(26, 5)
def num_effectively_unique_keys():
  """Calculates the number of effectively unique keys for the Playfair cipher."""
  return num_possible_keys() / (26 / 2**26)
if __name__ == "__main__":
  print("The Playfair cipher has", num_possible_keys(), "possible keys.")
  print("The Playfair cipher has", num_effectively_unique_keys(), "effectively unique keys.")
