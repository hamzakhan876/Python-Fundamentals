try:
 
 file = open("data.txt")

except FileNotFoundError:

    print("Error: File not found.")

else:
 print("File opened successfully.")

finally:
  print("Execution completed.")
  