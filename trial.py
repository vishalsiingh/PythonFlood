import os
# os.rename("cluster/bout.txt","cluster/cluster.txt")
# files = os.listdir("cluster")

files = os.listdir("Trial")
# print(files)
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"Trial/{file}", f"Trial/{i}.png")
    i = i + 2