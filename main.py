FILE_NAME = "ExpertPlus.dat"
BEAT_SHIFT = 5

with open(FILE_NAME, mode="r+") as source:
    with open(FILE_NAME.replace(".dat", "Fix.dat"), mode="w+") as destination:
        lines = source.readlines()
        for l in lines:
            new_line = l
            if "\"b\":" in l or "\"tb\":" in l:
                split = l.split(":")
                new_line = split[0] + ": " + str(float(split[1][0:len(split[1]) - 2]) + BEAT_SHIFT) + ",\n"

            destination.write(new_line)