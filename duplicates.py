import os

try:
    packagesInPPC64LE = os.listdir("/home/output/linux-ppc64le")
    print(packagesInPPC64LE)
except Exception:
    print("linux-ppc64le folder not found")

try:
    packagesInNoarch = os.listdir("/home/output/noarch")
    print(packagesInNoarch)
except Exception:
    print("noarch folder not found")
