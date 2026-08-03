file = None
INFO_count = 0
WARNING_count = 0
ERROR_count = 0

try:
    file = open("logs.txt", "r")

except FileNotFoundError:
    print("Error: File not found")
else:
    for line in file:

     if "INFO" in line:
        INFO_count += 1

     elif "WARNING" in line:
        WARNING_count += 1

     elif "ERROR" in line:
        ERROR_count += 1

finally:
     if file:
        file.close()

print("Program finished")
print("========= LOG FILE ANALYZER =========")
print(f"INFO: {INFO_count}")
print(f"WARNING: {WARNING_count}")
print(f"ERROR: {ERROR_count}")


    