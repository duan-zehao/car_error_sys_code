# 监测控制模块

import time

# 当前界面标签网址
jmbq_url_old = 'https://transport-safe.jd.com/transportSafety/process'

bj_url = 'https://transport-safe.jd.com/transportSafety'
bj_bq = '/process'

current_url = ''
title = ''
page_source = ''

sys_user_kgzt_jl = False

bjjmbs = True

sys_zt = False


def Voice_use(shared_chrome_Voice_user_run_ing,
              shared_chrome_Voice_text, shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, text):
    if not shared_chrome_Voice_user_run_ing.value:
        return

    shared_chrome_Voice_text_grade.value = True
    while shared_chrome_Voice_text.value != -1:
        pass

    for char in text:
        shared_chrome_Voice_text.value = ord(char)
        while shared_chrome_Voice_text.value != -1:
            if not shared_chrome_Voice_user_run_ing.value:
                shared_chrome_Voice_text.value = -1
                return
            pass

    shared_chrome_Voice_text_send_user.value = True


# 获取页面及界面相关信息
def hq_ym_jm_xx(shared_chrome_title_queue, shared_chrome_current_url_queue, shared_chrome_page_source_queue):
    global current_url
    global title
    global page_source
    global sys_zt

    title = shared_chrome_title_queue.get()
    if title == "!":
        sys_zt = False

    current_url = shared_chrome_current_url_queue.get()
    if current_url == "!":
        sys_zt = False

    page_source = shared_chrome_page_source_queue.get()
    if page_source == "!":
        sys_zt = False


# 报警页面及报警界面切换检测
def bjym_bjjm_qh_jc(shared_chrome_Voice_user_run_ing,
                    shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                    shared_chrome_error_jc_word_zt):
    global jmbq_url_old
    global bjjmbs

    if current_url != jmbq_url_old:
        jmbq_url_old = current_url
        if bjjmbs:
            bjjmbs = False
            if shared_chrome_error_jc_word_zt.value:
                shared_chrome_error_jc_word_zt.value = False
            bjtxkg_clean(shared_chrome_Voice_user_run_ing,
                         shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text)
        time.sleep(1)
        return True
    return False


# 打开报警提醒开关
def bjtxkg_open(shared_chrome_Voice_user_run_ing,
                shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text):
    global sys_user_kgzt_jl

    if not sys_user_kgzt_jl:
        Voice_use(shared_chrome_Voice_user_run_ing,
                  shared_chrome_Voice_text, shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade,
                  '报警提醒功能已打开')
        sys_user_kgzt_jl = True


# 关闭报警提醒开关
def bjtxkg_clean(shared_chrome_Voice_user_run_ing,
                 shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text):
    global sys_user_kgzt_jl

    if sys_user_kgzt_jl:
        Voice_use(shared_chrome_Voice_user_run_ing,
                  shared_chrome_Voice_text, shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade,
                  '报警提醒功能已关闭')
        sys_user_kgzt_jl = False


# 判断当前页面标签
def pddqymbq():
    if title == "运输安全管理平台":
        return True
    return False


# 判断界面标签是否为报警检测标签
def pdjmbq(shared_chrome_Voice_user_run_ing,
           shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
           shared_chrome_error_jc_word_zt):
    global bjjmbs

    jmbq_url_new = current_url[current_url.rfind('/')::]
    if bj_bq == jmbq_url_new:
        return True
    if shared_chrome_error_jc_word_zt.value:
        shared_chrome_error_jc_word_zt.value = False
    bjtxkg_clean(shared_chrome_Voice_user_run_ing,
                 shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text)
    return False


# 判断报警页面
def pdbjym(shared_chrome_Voice_user_run_ing,
           shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
           shared_chrome_error_jc_word_zt):
    if not pddqymbq():
        if shared_chrome_error_jc_word_zt.value:
            shared_chrome_error_jc_word_zt.value = False
        bjtxkg_clean(shared_chrome_Voice_user_run_ing,
                     shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text)
        return False
    return True


def pd_user_kg_zt(shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                  shared_chrome_error_jc_word_zt, shared_chrome_Voice_user_run_ing):
    global bjjmbs

    if page_source.find("el-checkbox freshBtn is-checked") == -1:
        if bjjmbs:

            if not shared_chrome_error_jc_word_zt.value:
                shared_chrome_error_jc_word_zt.value = True
            bjtxkg_open(shared_chrome_Voice_user_run_ing,
                        shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text)
            return True
    elif page_source.find("el-checkbox freshBtn is-checked") != -1:
        if not bjjmbs:
            bjjmbs = True
        if shared_chrome_error_jc_word_zt.value:
            shared_chrome_error_jc_word_zt.value = False
        bjtxkg_clean(shared_chrome_Voice_user_run_ing,
                     shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text)
    return False


# 检测模块启动函数
def jcmk_start(shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
               shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
               shared_chrome_jccz_page_source_queue, shared_chrome_jccz_current_url_queue,
               shared_chrome_jccz_title_queue,
               shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
               shared_chrome_error_jc_word_zt, shared_chrome_Voice_user_run_ing):
    global sys_zt

    while shared_chrome_process_s_jcmk_run_zt.value:
        if not shared_chrome_process_s_jcmk_run_ing.value:
            shared_chrome_process_s_jcmk_run_ing.value = True

        if (not shared_chrome_jcmk_run_zt.value) and shared_chrome_jcmk_run_ing.value:
            shared_chrome_jcmk_run_ing.value = False
            shared_chrome_error_jc_word_zt.value = False
            sys_zt = False

        while shared_chrome_jcmk_run_zt.value:
            if not shared_chrome_jcmk_run_ing.value:
                sys_zt = True
                shared_chrome_jcmk_run_ing.value = True

            if not sys_zt:
                continue
            # 获取页面与界面相关信息
            hq_ym_jm_xx(shared_chrome_jccz_title_queue, shared_chrome_jccz_current_url_queue,
                        shared_chrome_jccz_page_source_queue)

            # 检测页面及界面是否发生过切换
            if bjym_bjjm_qh_jc(shared_chrome_Voice_user_run_ing, shared_chrome_Voice_text_send_user,
                               shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                               shared_chrome_error_jc_word_zt):
                continue

            # 判断是否为报警页面
            if not pdbjym(shared_chrome_Voice_user_run_ing, shared_chrome_Voice_text_send_user,
                          shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                          shared_chrome_error_jc_word_zt):
                continue

            # 判断是否为报警界面
            if not pdjmbq(shared_chrome_Voice_user_run_ing, shared_chrome_Voice_text_send_user,
                          shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                          shared_chrome_error_jc_word_zt):
                continue

            # 判断用户可操作开关的状态
            pd_user_kg_zt(shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
                          shared_chrome_error_jc_word_zt, shared_chrome_Voice_user_run_ing)

    if (not shared_chrome_process_s_jcmk_run_zt.value) and shared_chrome_process_s_jcmk_run_ing.value:
        shared_chrome_process_s_jcmk_run_ing.value = False
