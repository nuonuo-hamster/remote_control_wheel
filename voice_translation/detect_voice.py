import argparse
import functools
import time

import numpy as np
import soundcard as sc
import multiprocessing

from macls.predict import MAClsPredictor
from macls.utils.utils import add_arguments, print_arguments

parser = argparse.ArgumentParser(description=__doc__)
add_arg = functools.partial(add_arguments, argparser=parser)
add_arg('configs',          str,    'configs/cam++.yml',   '配置文件')
add_arg('use_gpu',          bool,   True,                  '是否使用GPU预测')
add_arg('record_seconds',   float,  3,                     '录音长度')
add_arg('model_path',       str,    'models/CAMPPlus_Fbank/best_model/', '导出的预测模型文件路径')
args = parser.parse_args()
# print_arguments(args=args)

# 获取识别器
predictor = MAClsPredictor(configs=args.configs,
                           model_path=args.model_path,
                           use_gpu=args.use_gpu)
# 获取默认麦克风
default_mic = sc.default_microphone()
# 录音采样率
samplerate = 16000
# 录音块大小
numframes = 1024
# 模型输入长度
infer_len = int(samplerate * args.record_seconds / numframes)

all_data = []

def infer_thread(prediction, lock):
   with lock:
        old_result = None

        s = time.time()
        while True:
            try:
                if prediction[1]: break 
                if len(all_data) < infer_len: continue
                # 截取最新的音频数据
                seg_data = all_data[-infer_len:]
                d = np.concatenate(seg_data)
                # 删除旧的音频数据
                del all_data[:len(all_data) - infer_len]
                label, score = predictor.predict(audio_data=d, sample_rate=samplerate)

                if score > 0.9 and label != old_result:
                    print(f'{int(time.time() - s)}s 预测结果标签为：{label}，得分：{score}')
                    old_result = label
                    prediction[0] = label
            except:
                pass

def mic_record(mic):

    data = mic.record(numframes=numframes)
    all_data.append(data)

def init(TKRoot):

    p = multiprocessing.Process(target=infer_thread, args=(TKRoot.prediction, TKRoot.lock))
    p.start()

    return default_mic.recorder(samplerate=samplerate, channels=1)

if __name__ == '__main__':

    prediction = [None]
    mic = init(prediction)

    with mic:
        while True:
            mic_record(mic)
