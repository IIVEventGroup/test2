import os
import sys
import shutil

path250_w2ms = os.path.join("/home/test4/code/EventBenchmark/lib/pytracking/data/EventSOT500","250_w2ms")
# if not os.path.exists(path250_w2ms):
#     os.mkdir(path250_w2ms)

# path500_w2ms = os.path.join("/home/test4/code/EventBenchmark/lib/pytracking/data/EventSOT500/500_w2ms")
# for seq in os.listdir(path500_w2ms):
#     source_path = os.path.join(path500_w2ms, seq)
#     dest_path = os.path.join(path250_w2ms, seq)
#     if not os.path.exists(dest_path):
#         shutil.copytree(source_path, dest_path)

for seq in os.listdir(path250_w2ms):
    seq=os.path.join(path250_w2ms,seq)
    #img deleted
    path_voxel_grid_complex=os.path.join(seq,"VoxelGridComplex")
    all_pngs=sorted([f for f in os.listdir(path_voxel_grid_complex) if f.endswith(".jpg")])
    pngs_to_save=all_pngs[::2]
    idx=0
    for png in all_pngs:
        if png not in pngs_to_save:
            png_path=os.path.join(path_voxel_grid_complex,png)
            os.remove(png_path)
            print(f"Deleted:{png_path}")
            continue
        else:
            new_img = f"{idx:05}.jpg"
            os.rename(os.path.join(path_voxel_grid_complex,png),os.path.join(path_voxel_grid_complex,new_img))
            idx+=1
    #annot deleted
    gt=os.path.join(seq,"groundtruth.txt")
    with open(gt,"r") as f:
        lines=f.readlines()
    lines=[line for idx,line in enumerate(lines) if idx%2==0]
    with open(gt,"w") as f:
        f.writelines(lines)