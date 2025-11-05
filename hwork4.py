web_dev = ["John", "Alice", "Mark"]
data_science = ["Sophia", "Liam", "Noah"]
ui_ux = ["Emma", "Olivia", "Ava"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("David")
data_science.insert(1, "Mia")
ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

print("First two Web Dev participants:", web_dev[:2])

name_lengths = [len(name) for name in data_science_copy]
print("Name lengths (Data Science copy):", name_lengths)

asha_exists = "Asha" in web_dev or "Asha" in data_science_copy or "Asha" in ui_ux
print("Is 'Asha' in any workshop list?", asha_exists)

first_participants = (web_dev[0], data_science_copy[0], ui_ux[0])
print("Tuple of first participants:", first_participants)
