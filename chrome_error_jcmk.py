import time

bjtxkg = -1  # 报警提醒开关

have_car = False  # 有车辆报警标识

chrome_start_bs = False

# 进程列表
chrome_processes_id = int
chrome_processes_s_id = []

# 报警界面标签
bjjmbq = 'process'

sys_zt = False


def Voice_use(shared_chrome_Voice_user_run_ing,
              shared_chrome_Voice_text, shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, text):
    if not shared_chrome_Voice_user_run_ing.value:
        return False

    if shared_chrome_Voice_text_grade.value:
        return False

    for char in text:
        shared_chrome_Voice_text.value = ord(char)
        while shared_chrome_Voice_text.value != -1:
            if shared_chrome_Voice_text_grade.value or (not shared_chrome_Voice_user_run_ing.value):
                if not shared_chrome_Voice_user_run_ing.value:
                    shared_chrome_Voice_text.value = -1
                return False

    shared_chrome_Voice_text_send_user.value = True
    return True


def sys_print_use(shared_chrome_message_text, shared_chrome_message_text_print, text):
    for char in text:
        shared_chrome_message_text.value = ord(char)
        while shared_chrome_message_text.value != -1:
            pass

    shared_chrome_message_text_print.value = True


def error_jc_yx_cx(shared_chrome_error_jc_word_zt):
    if shared_chrome_error_jc_word_zt.value:
        return True
    return False


def bjjc(shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
         shared_chrome_error_page_source_queue, shared_chrome_find_button_zt, shared_chrome_Voice_user_run_ing,
         shared_chrome_error_jc_word_zt):
    global sys_zt
    # 当前页面为登录页面或禁止刷新未被取消勾选时则不开启警报
    page_source = shared_chrome_error_page_source_queue.get()
    if page_source == "!":
        sys_zt = False
        return

    if page_source.find("el-table__empty-block") == -1:
        if not error_jc_yx_cx(shared_chrome_error_jc_word_zt):
            return
        if not Voice_use(shared_chrome_Voice_user_run_ing,
                         shared_chrome_Voice_text, shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade,
                         "风险车辆已产生"):
            return
        if not shared_chrome_find_button_zt.value:
            shared_chrome_find_button_zt.value = True
            time.sleep(2)

        if page_source.find("el-table__empty-block") == -1:
            if not error_jc_yx_cx(shared_chrome_error_jc_word_zt):
                return
            if not Voice_use(shared_chrome_Voice_user_run_ing,
                             shared_chrome_Voice_text, shared_chrome_Voice_text_send_user,
                             shared_chrome_Voice_text_grade, "请及时处理"):
                return

            if not shared_chrome_find_button_zt.value:
                shared_chrome_find_button_zt.value = True
                time.sleep(2)


def chrome_error_jc_start(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                          shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                          shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                          shared_chrome_error_jc_word_zt, shared_chrome_error_page_source_queue,
                          shared_chrome_find_button_zt,
                          shared_chrome_Voice_user_run_ing
                          ):
    global sys_zt
    while shared_chrome_process_s_error_jc_run_zt.value:
        if not shared_chrome_process_s_error_jc_run_ing.value:
            shared_chrome_process_s_error_jc_run_ing.value = True

        if (not shared_chrome_error_jc_run_zt.value) and shared_chrome_error_jc_run_ing.value:
            sys_zt = False
            shared_chrome_error_jc_run_ing.value = False

        while shared_chrome_error_jc_run_zt.value:
            if not shared_chrome_error_jc_run_ing.value:
                sys_zt = True
                shared_chrome_error_jc_run_ing.value = True

            if shared_chrome_error_jc_word_zt.value and sys_zt:
                bjjc(shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                     shared_chrome_error_page_source_queue, shared_chrome_find_button_zt,
                     shared_chrome_Voice_user_run_ing, shared_chrome_error_jc_word_zt)

    if (not shared_chrome_process_s_error_jc_run_zt.value) and shared_chrome_process_s_error_jc_run_ing.value:
        shared_chrome_process_s_error_jc_run_ing.value = False
