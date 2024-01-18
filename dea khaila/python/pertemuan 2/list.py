makanan = ["nasi kuning", "nasi goreng", "ayam geprek"]
minuman = ["es teh", "extra joss", "coca-cola"]

print(makanan)
print(minuman)

print(minuman[1])
print(len(minuman))

minuman[1] = "kukubima"
del minuman[1]
print(minuman)
makanan.append("chicken katsu")
print(makanan)