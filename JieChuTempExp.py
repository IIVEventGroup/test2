import sys
sys.path.append('/home/test4/code/EventBenchmark/lib/pytracking/')

import os
import sys
import shutil
import subprocess
import matplotlib.pyplot as plt
from pytracking.evaluation import Tracker, get_dataset, trackerlist, load_stream_setting
from pytracking.analysis.plot_results import plot_results, print_results, print_per_sequence_results, plot_results_mod

run_rounds=5
cuda_index=2

if False:
    # 定义要运行的命令：跑5轮实验
    command_exp = f"CUDA_VISIBLE_DEVICES={cuda_index} python /home/test4/code/EventBenchmark/lib/pytracking/pytracking/run_experiment_streaming.py exp_streaming streaming_31_{run_rounds}range"

    # 使用 subprocess 运行命令
    try:
        subprocess.run(command_exp, shell=True, check=True)
        print("命令成功运行")
    except subprocess.CalledProcessError as e:
        print(f"命令运行失败，返回码：{e.returncode}")
    except Exception as ex:
        print(f"发生了其他错误：{str(ex)}")


for FPS in [20,50,125,250,500]:
    if FPS!=20:
        # 定义要运行的命令：按照FPS频率的annotation的规格对齐5轮实验的结果
        command_align = f"CUDA_VISIBLE_DEVICES={cuda_index} python /home/test4/code/EventBenchmark/lib/pytracking/eval/streaming_eval_v4_JieChu.py exp_streaming streaming_31_5range --FPS {FPS}"

        # 使用 subprocess 运行命令
        try:
            subprocess.run(command_align, shell=True, check=True)
            print("命令成功运行")
        except subprocess.CalledProcessError as e:
            print(f"命令运行失败，返回码：{e.returncode}")
        except Exception as ex:
            print(f"发生了其他错误：{str(ex)}")


    #评估实验结果
    trackers = []
    run_id = range(run_rounds)
    trackers.extend(trackerlist(name='atom', parameter_name='default',
                                run_ids=run_id, display_name='atom'))
    trackers.extend(trackerlist(name='atom', parameter_name='fe240',
                                run_ids=run_id, display_name='atom_fe240'))
    trackers.extend(trackerlist(name='dimp', parameter_name='dimp18', 
                                run_ids=run_id, display_name='dimp18'))
    trackers.extend(trackerlist(name='dimp', parameter_name='dimp18_fe240', 
                                run_ids=run_id, display_name='dimp18_fe240'))
    trackers.extend(trackerlist(name='dimp', parameter_name='prdimp18', 
                                run_ids=run_id, display_name='prdimp18'))
    trackers.extend(trackerlist(name='dimp', parameter_name='dimp50', 
                                run_ids=run_id, display_name='dimp50'))
    trackers.extend(trackerlist(name='kys', parameter_name='default', 
                                run_ids=run_id, display_name='kys'))
    trackers.extend(trackerlist(name='kys', parameter_name='fe240', 
                                run_ids=run_id, display_name='kys_fe240'))
    trackers.extend(trackerlist(name='rts', parameter_name='rts50', 
                                run_ids=run_id, display_name='rts50'))
    trackers.extend(trackerlist(name='keep_track', parameter_name='default', 
                                run_ids=run_id, display_name='keep_track'))
    trackers.extend(trackerlist(name='tomp', parameter_name='tomp50', 
                                run_ids=run_id, display_name='tomp50'))
    stream_setting_id = 31
    dataset_name = 'esot500s'
    dataset = get_dataset(dataset_name,annot_fps=FPS)

    print_results(trackers, dataset, dataset_name, merge_results=False, plot_types=('success', 'prec', 'norm_prec'),force_evaluation=True, stream_id=stream_setting_id,
        results_saved_file=f'/home/test4/code/EventBenchmark/lib/pytracking/pytracking/analysis/JieChuExp_11trackers_{FPS}fps.txt')