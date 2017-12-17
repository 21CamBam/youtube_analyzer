import os
from os.path import join, getsize

depth = -1

DEPTHS = ["depth_zero.csv", "depth_one.csv", "depth_two.csv", "depth_three.csv", "depth_four.csv", "related_videos.csv"]

raw_data_dir = "/ifs/home/csmith2/Other/youtube_analyzer/unprocessed_data/"
uncondensed_data_dir = "/ifs/home/csmith2/Other/youtube_analyzer/unzip"

dirs = [d for d in os.listdir(uncondensed_data_dir)]

for d in dirs:
    files = [f for f in os.listdir("{0}/{1}".format(uncondensed_data_dir,d))]
    for f in files:
        count = 0
        try:
            depth = int(f.split('.')[0])
        except:
            continue # skip log file
        with open("{0}/{1}/{2}".format(uncondensed_data_dir,d,f)) as input_file:
            with open("{0}/{1}".format(raw_data_dir,DEPTHS[depth]), "a") as output_file:
                print "Processing {0}/{1}...".format(d,f)
                for line in input_file:
                    try: # eliminate incomplete data
                        new_line = []
                        elements = line.split()
                        video_id = elements[0]
                        for i in range(0, 10):
                            if i == 3: # Category
                                cat_end = False
                                category = []
                                while not cat_end:
                                    try:
                                        int(elements[i]) # if this works, we're done
                                        cat_end = True
                                    except:
                                        category.append(elements[i])
                                        del elements[i]
                                new_line.append(" ".join(category))
                                new_line.append(elements[i])
                            elif i == 8: # Begin related video_ids
                                with open("{0}/{1}".format(raw_data_dir,DEPTHS[-1]), "a") as related_file:
                                    for j in range(i, len(elements)):
                                        related_file.write("{0}, {1}\n".format(video_id, elements[j]))
                                break
                            else:
                                new_line.append(elements[i])
                        output_file.write(", ".join(new_line) + "\n")
                    except:
                        continue
