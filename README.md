# Password Hasher
A small terminal application to hash a password and save the hash as a .txt.

This was made whilst creating a flask application. I wanted an admin and general user, but everytime I reset the development server it would wipe the database. This was a way to initialise the database with the hashes input. I did not want to type the main password into the key code and hash it that way, as it would mean that the original passwords are easy to find.

This application hashes in Sha256, but could be adjusted.
