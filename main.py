from package_hasher import PackageHashMap

def main():
    print("Hello, python")
    package_map = PackageHashMap(40)
    print(package_map.package_hash_function("a","2","3","4","5","6"))

main()
