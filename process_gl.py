# 线程管理器
import multiprocessing

Process_ml = []


# 线程的注册
def Process_add(target, args):
    Process_name = multiprocessing.Process(target=target, args=args)
    Process_ml.append(Process_name)
    return Process_name


# 线程的启动
def Process_start(process_name):
    Process_id = Process_ml.index(process_name)
    Process_ml[Process_id].start()


def Process_stop(process_name, shared_process_stop_bz):
    Process_id = Process_ml.index(process_name)
    if Process_id == 2:
        Process_ml[Process_id].terminate()
    else:
        Process_ml[Process_id].join()

    Process_ml.pop(Process_id)
    shared_process_stop_bz.value = True
