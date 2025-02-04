# Operatorên di Python ê de

# 1. Operatorên Aritmetîk
a = 5
b = 3
# +  Zêdek: Du nirxan li hev zêde dike.
print(a + b)
# -  Kêmek: Nirxa duyemîn ji yekemîn der dixe.
print(a - b)
# *  Lêkdan: Du nirxan li hev dixe.
print(a * b)
# /  Parvek: Nirxa yekemîn ji nirxa duyemîn re parve dike.
print(a / b)
# %  Mod: Bakiya parvekirina nirxa yekemîn ji nirxa duyemîn re vedide.
print(a % b)
# ** # Hêzek: Nirxa yekemîn bi hêza nirxa duyemîn vedike.
print(a ** b)
# // # Parvekirina Tam: Nirxa yekemîn ji nirxa duyemîn re parve dike û encam wekî hejmarên tam vedide.
print(a // b)


# 2. Operatorên Berhevokê
a = 5
b = 3
c = 5
# == # Yeksan: Nirxên du yeksan in heye kontrol dike.
print(a == b)
print(a == c)
# != # Ne Yeksan: Nirxên du neyeksan in heye kontrol dike.
print(a != b)
print(a != c)
# >  # Mezin: Nirxa çep ji nirxa rast mezintir heye kontrol dike.
print(a > b)
# <  # Biçûk: Nirxa çep ji nirxa rast biçûktir heye kontrol dike.
print(a < b)
# >= # Mezin an Yeksan: Nirxa çep ji nirxa rast mezintir an yeksan heye kontrol dike.
print(a >= b)
print(a >= c)
# <= # Biçûk an Yeksan: Nirxa çep ji nirxa rast biçûktir an yeksan heye kontrol dike.
print(a >= b)
print(a >= c)

# 3. Operatorên Mantîkî

a = True
b = True
c = False
d = True
# and # Û: Hemî du ifadên rast in ger rast vedibe.
print(a and b)
print(a and b and c and d)
# or  # An: Yek ji ifadên rast heye ger rast vedibe.
print(a and c)
print(a and b and c and d)
# not # Ne: Nirxa mantîkî ya ifadeyê diguherîne.
print(not a)
print(not c)


# 4. Operatorên Astê
# &  # AND: Li astê û dike.
# |  # OR: Li astê an dike.
# ^  # XOR: Li astê taybetî an dike.
# ~  # NOT: Li astê ne, hemî bitan diguherîne.
# << # Rast Guhertin: Bitên nirxa çep bi qasî nirxa rast guherandî rast dike.
# >> # Çep Guhertin: Bitên nirxa çep bi qasî nirxa rast guherandî çep dike.

# 5. Operatorên Endamtiyê
a = 'kurdistan'
b = 'kurd'
# in    # Endam: Di koleksiyonek de, yek eleman heye kontrol dike.
print(a in b)
# not in # Ne Endam: Di koleksiyonek de, yek eleman tune heye kontrol dike.
print(a not in b)


# 6. Operatorên Nasnameyê
a = [1,2]
b = [1,2]
# is    # Nasname: Dureferansên du yên objeyê yek bi yek têne kontrol kirin.
print(a is b)
# is not# Ne Nasname: Dureferansên du objeyên cûda têne kontrol kirin.
print(a is not b)

# 7. Operatorên Danînê
# =   # Danîna Sade: Nirxa rast li nirxa çep tê dayîn. 
a, b, c = 5,3,7
# +=  # Lêzêdekirina Danînê: Nirxa rast li nirxa çep tê zêdekirin û encam li nirxa çep tê dayîn.
a = a + b
a += b
# -=  # Bikêşandina Danînê: Nirxa rast ji nirxa çep tê xistin û encam li nirxa çep tê dayîn.
a = a - b
a -= b
# *=  # Vezirandina Danînê: Nirxa rast bi nirxa çep tê vezirandin û encam li nirxa çep tê dayîn.
a = a * b
a *= b
# /=  # Parvekirina Danînê: Nirxa rast ji nirxa çep re tê parvekirin û encam li nirxa çep tê dayîn.
a = a / b
a /= b
# %=  # Moda Danînê: Nirxa rast ji nirxa çep re tê mod kirin û encam li nirxa çep tê dayîn.
a = a % b
a %= b
# **= # Hêzeka Danînê: Nirxa rast wekî hêza nirxa çep tê hesibandin û encam li nirxa çep tê dayîn.
a = a ** b
a **= b
# //= # Parvekirina Tama Danînê: Nirxa rast ji nirxa çep re tê parvekirin û encam wekî hejmarên tam li nirxa çep tê dayîn.
a = a // b
a //= b
print(a)