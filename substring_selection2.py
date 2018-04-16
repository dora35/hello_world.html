sample_string = "<div class='keyword'>Friendly</div>"

start_position_number = sample_string.find("'keyword'>")

start_position_number += 10

end_position_number = sample_string.find("<", start_position_number)

our_substring = sample_string[start_position_number:end_position_number]

print(our_substring)