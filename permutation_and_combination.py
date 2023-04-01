def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    return factorial(n) / factorial(n - r)

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
#-------------------------
#ODEV-1
# Soru: Anne ile Baba yanyana oturmak şartıyla yuvarlak masa etrafına kaç farklı şekilde oturabilirler?
# Diğer 3 kişinin masada oturabileceği şekil sayısı
other_people = factorial(3)
# Anne ve Baba yer değiştirebilir, bu nedenle sonuç 2 ile çarpılır.
result_a = 2 * other_people
print("a) Toplam şekil sayısı:", result_a)

# Soru: Anne ile Baba yanyana oturmamak şartıyla yuvarlak masa etrafına kaç farklı şekilde oturabilirler?
# Tüm durumlardan Anne ve Baba'nın yan yana oturdukları şekil sayısı çıkarılır.
all_permutations = factorial(5 - 1)
result_b = all_permutations - result_a
print("b) Toplam şekil sayısı:", result_b)

# Soru: Çocuklar yan yana oturmak şartıyla yuvarlak masa etrafında kaç farklı şekilde oturabilirler?
# 3 çocuk tek bir birim olarak ele alınırsa, masada çevresindeki şekil sayısı (3-1)! = 2'dir.
# Çocuklar bir arada oturduğunda, 3! = 6 farklı şekilde oturabilirler.
# Bu nedenle, çocukların oturma şekilleri toplamda 2 * 6 = 12 farklı olabilir.
children_group = factorial(3)
result_c = 2 * children_group
print("c) Toplam şekil sayısı:", result_c)

#-------------------------
#ODEV-2
# Soru: 4 erkek ve 5 kız arasından en az birinin kız olduğu 3 kişilik bir grup kaç farklı şekilde oluşturulabilir?
# Oluşturulabilecek toplam 3 kişilik grupların sayısı
total_permutations = combination(9, 3)
# İçinde hiç kız olmadan oluşturulabilecek 3 kişilik grupların sayısı
boys = combination(4, 3)
# En az bir kız içeren 3 kişilik grupların sayısı
girls = int(total_permutations - boys)
print("d) En az bir kızın olduğu grup sayısı:", girls)
# En az bir kızın olduğu grup sayısı, toplam grupların sayısından sadece erkeklerden oluşan grupların sayısının çıkarılmasıyla hesaplanabilir.