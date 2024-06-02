import tkinter as tk

sys_run_ing = True

root = tk.Tk()
chrome_start_button = tk.Button(root)
main_sys_stop_button = tk.Button(root)
chrome_driver_process_label = tk.Label(root)
chrome_driver_run_label = tk.Label(root)
chrome_message_label = tk.Label(root)
chrome_process_s_label = tk.Label(root)
chrome_run_s_label = tk.Label(root)
chrome_error_jc_process_label = tk.Label(root)
chrome_error_jc_run_label = tk.Label(root)
jcmk_process_label = tk.Label(root)
jcmk_run_label = tk.Label(root)
Voice_user_process_label = tk.Label(root)
Voice_user_run_label = tk.Label(root)
Voice_work_label = tk.Label(root)

chrome_start_button_text = ''
chrome_driver_process_label_text = ''
chrome_driver_run_label_text = ''
chrone_message_label_text = ''
chrome_process_s_label_text = ''
chrome_run_s_label_text = ''
chrome_error_jc_process_label_text = ''
chrome_error_jc_run_label_text = ''
jcmk_process_label_text = ''
jcmk_run_label_text = ''
Voice_user_process_label_text = ''
Voice_user_run_label_text = ''
Voice_work_label_text = ''

main_process = []

chrome_message_text = '无'
chrome_message_text_sleep = ''


def chrome_message_text_updata(shared_chrome_message):
    global chrome_message_text_sleep

    if shared_chrome_message.value == -1:
        return

    chrome_message_text_sleep += chr(shared_chrome_message.value)
    shared_chrome_message.value = -1


def label_text_update(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
                      shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
                      shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
                      shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
                      shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                      shared_chrome_message_text_print, shared_chrome_message_text):
    global chrome_start_button_text
    global chrome_driver_process_label_text
    global chrome_driver_run_label_text
    global chrone_message_label_text
    global chrome_process_s_label_text
    global chrome_run_s_label_text
    global chrome_error_jc_process_label_text
    global chrome_error_jc_run_label_text
    global jcmk_process_label_text
    global jcmk_run_label_text
    global Voice_user_process_label_text
    global Voice_user_run_label_text
    global chrome_message_text
    global chrome_message_text_sleep

    chrome_message_text_updata(shared_chrome_message_text)
    if shared_chrome_message_text_print.value:
        chrome_message_text = chrome_message_text_sleep
        chrome_message_text_sleep = ''
        shared_chrome_message_text_print.value = False

    chrone_message_label_text = chrome_message_text
    chrome_driver_process_label_text = '已启动' if shared_chrome_driver_process_run_ing.value else '已关闭'
    chrome_driver_run_label_text = '运行中' if shared_chrome_driver_run_ing.value else '未运行'
    chrome_process_s_label_text = '已启动' if shared_chrome_process_s_run_ing.value else '已关闭'
    chrome_run_s_label_text = '运行中' if shared_chrome_s_run_ing.value else '未运行'
    chrome_error_jc_process_label_text = '已启动' if shared_chrome_process_s_error_jc_run_ing.value else '已关闭'
    chrome_error_jc_run_label_text = '运行中' if shared_chrome_error_jc_run_ing.value else '未运行'
    jcmk_process_label_text = '已启动' if shared_chrome_process_s_jcmk_run_ing.value else '已关闭'
    jcmk_run_label_text = '运行中' if shared_chrome_jcmk_run_ing.value else '未运行'
    Voice_user_process_label_text = '已启动' if shared_chrome_process_s_Voice_user_run_ing.value else '已关闭'
    Voice_user_run_label_text = '运行中' if shared_chrome_Voice_user_run_ing.value else '未运行'

    chrome_start_button_text = '启动浏览器' if not shared_chrome_driver_run_ing.value else '关闭浏览器'


def chrome_start_user_stop_cz(shared_chrome_start):
    shared_chrome_start.value = False


def chrome_start_user_start_cz(shared_chrome_start):
    shared_chrome_start.value = True


def main_sys_stop_cz(shared_main_sys_zt):
    root.quit()
    shared_main_sys_zt.value = False


# 窗口界面显示与功能按键配置
def win_jm_gnaj():
    global chrome_driver_process_label
    global chrome_driver_run_label
    global chrome_message_label
    global chrome_process_s_label
    global chrome_run_s_label
    global chrome_error_jc_process_label
    global chrome_error_jc_run_label
    global jcmk_process_label
    global jcmk_run_label
    global Voice_user_process_label
    global Voice_user_run_label
    global chrome_start_button
    global main_sys_stop_button

    global root

    root.title("车辆提醒报警系统")

    sys_label = tk.Label(root, text='控制界面')
    sys_label.pack(padx=10, pady=10)
    chrome_driver_process_label.pack(padx=10, pady=10)
    chrome_driver_run_label.pack(padx=10, pady=10)
    chrome_process_s_label.pack(padx=10, pady=10)
    chrome_run_s_label.pack(padx=10, pady=10)
    chrome_error_jc_process_label.pack(padx=10, pady=10)
    chrome_error_jc_run_label.pack(padx=10, pady=10)
    jcmk_process_label.pack(padx=10, pady=10)
    jcmk_run_label.pack(padx=10, pady=10)
    Voice_user_process_label.pack(padx=10, pady=10)
    Voice_user_run_label.pack(padx=10, pady=10)

    chrome_message_label.pack(padx=10, pady=10)

    chrome_start_button.pack(pady=10)
    main_sys_stop_button.pack(pady=10)


def win_update(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
               shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
               shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
               shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
               shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
               shared_chrome_message_text_print, shared_chrome_message_text,
               shared_chrome_start, shared_main_sys_zt, shared_sys_reset):
    global chrome_driver_process_label
    global chrome_driver_run_label
    global chrome_process_s_label
    global chrome_run_s_label
    global chrome_error_jc_process_label
    global chrome_error_jc_run_label
    global jcmk_process_label
    global jcmk_run_label
    global Voice_user_process_label
    global Voice_user_run_label
    global Voice_print_process_label
    global Voice_print_run_label
    global chrome_start_button
    global main_sys_stop_button
    global root

    label_text_update(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
                      shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
                      shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
                      shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
                      shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                      shared_chrome_message_text_print, shared_chrome_message_text)
    chrome_driver_process_label.config(text="浏览器进程状态：" + chrome_driver_process_label_text)
    chrome_driver_run_label.config(text='浏览器运行状态：' + chrome_driver_run_label_text)
    chrome_process_s_label.config(text="浏览器子进程总状态：" + chrome_process_s_label_text)
    chrome_run_s_label.config(text='浏览器子模块运行状态：' + chrome_run_s_label_text)
    chrome_error_jc_process_label.config(text="车辆报警检测模块进程状态：" + chrome_error_jc_process_label_text)
    chrome_error_jc_run_label.config(text="车辆报警检测模块运行状态：" + chrome_error_jc_run_label_text)
    jcmk_process_label.config(text="报警检测模块进程状态：" + jcmk_process_label_text)
    jcmk_run_label.config(text='报警检测模块运行状态：' + jcmk_run_label_text)
    Voice_user_process_label.config(text="扬声器控制模块进程状态：" + Voice_user_process_label_text)
    Voice_user_run_label.config(text='扬声器控制模块运行状态：' + Voice_user_run_label_text)
    chrome_message_label.config(text='浏览器消息：' + chrone_message_label_text)
    chrome_start_button.config(text=chrome_start_button_text, command=lambda: chrome_start_user_start_cz(
        shared_chrome_start) if chrome_start_button_text == '启动浏览器' else chrome_start_user_stop_cz(
        shared_chrome_start))

    if not shared_chrome_driver_process_run_ing.value:
        main_sys_stop_button.pack(pady=10)
        # if not shared_sys_reset.value:
        #     main_sys_stop_button.config(text='关闭主程序')
            # while not shared_sys_reset.value:
            #     pass
        main_sys_stop_button.config(text="关闭主程序", command=lambda: main_sys_stop_cz(shared_main_sys_zt))
    else:
        main_sys_stop_button.pack_forget()

    root.after(1, lambda: win_update(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
                                     shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
                                     shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
                                     shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
                                     shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                                     shared_chrome_message_text_print, shared_chrome_message_text,
                                     shared_chrome_start, shared_main_sys_zt, shared_sys_reset))


def sys_print(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
              shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
              shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
              shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
              shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
              shared_chrome_message_text_print, shared_chrome_message_text,
              shared_chrome_start, shared_main_sys_zt, shared_sys_reset):
    win_jm_gnaj()
    win_update(shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
               shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
               shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
               shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
               shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
               shared_chrome_message_text_print, shared_chrome_message_text,
               shared_chrome_start, shared_main_sys_zt, shared_sys_reset)
    root.mainloop()
