from functions.get_files_info import get_files_info

print("Result for current directory:")
print(get_files_info("calculator", "."))
print()  # blank line for readability

print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))
print()

print("Result for 'outside working dir' error:")
print(get_files_info("calculator", "/bin"))
print()

print("Result for 'outside working dir' error, again:")
print(get_files_info("calculator", "../"))
print()