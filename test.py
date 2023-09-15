import hashing_functions

try_message = b'O+n/smUA7e+83uNrcXgcc24Q0uuAysjQgE3XPb8n6MCGab3v360DJNrX16lr5qLYFcv6G2CJNmtguKGnf9OexNTqU5jXQEHSRNt6/0m0GDR1XcQzbwI9BTl11IfuJ2srBEa1kLz/AgszFQeUnGthO7yTVyack7UcO7scF6qfc3o='
# message = hashing_functions.encrypt("this message should read as '<INSERT TEXT HERE>'")
# print(f"The encrypted text is: {message}")
readable_message = hashing_functions.decrypt(try_message)
print(f"\nAnd the decrypted version reads '{readable_message}'\n")

