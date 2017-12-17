import os
from os.path import join, getsize

depth = -1

DEPTHS = ["depth_zero.csv", "depth_one.csv"]

DEPTHS_JSON = ["depth_zero.json", "depth_one.json"]

fields = ["video_id", "uploader", "video_age", "category", "video_length", "num_views", "rate", "num_ratings", "num_comments"]
fields2 = ["video_id1", "video_id2"]

raw_data_dir = "/ifs/home/csmith2/Other/youtube_analyzer/unprocessed_data/"

for j in range(0, len(DEPTHS)):
    count = 0
    with open("{0}/{1}".format(raw_data_dir,DEPTHS[j])) as input_file:
        with open("{0}/{1}".format(raw_data_dir,DEPTHS_JSON[j]), "a") as output_file:
            print "Processing {0}...".format(DEPTHS[depth])
            for line in input_file:
                count += 1
                print count
                try: # eliminate incomplete data
                    elements = line.strip().split(", ")
                    for i in range(0, 9):
                        try:
                            foo = int(elements[i])
                            elements[i] = "\"{0}\": {1}".format(fields[i], elements[i])
                        except:
                            elements[i] = "\"{0}\": \"{1}\"".format(fields[i], elements[i])
                    output_file.write("{" + ", ".join(elements) + "}\n")
                except:
                    continue

count = 0
print "Processing related_videos.csv..."
with open("{0}/{1}".format(raw_data_dir,"related_videos.csv")) as input_file:
    with open("{0}/{1}".format(raw_data_dir, "related_videos.json"), "a") as output_file:
        for line in input_file:
            count += 1
            print count
            try: # eliminate incomplete data
                elements = line.strip().split(", ")
                for i in range(0, 2):
                    elements[i] = "\"{0}\": \"{1}\"".format(fields2[i], elements[i])
                output_file.write("{" + ", ".join(elements) + "}\n")
            except:
                continue
