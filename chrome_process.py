from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
import os
# import main.configs.file_dir_id
import file_dir_id

user_data_up = False  # 用户数据更新标识

# 页面标签网址
ymbq_url = 'https://transport-safe.jd.com/transportSafety'
# 界面标签网址
jmbq_url = '/process'

# 登录页面网址
login_url = ymbq_url + jmbq_url

chrome_driver_ing = False

# 进程列表
chrome_processes_id = int
chrome_processes_s_id = []


# 浏览器配置
def chrome_config():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    chrome_driver_path = os.path.join(current_dir, "../chromedriver1.exe")

    chrome_options = Options()
    service = Service(chrome_driver_path)

    chrome_run_yl = [chrome_options, service]
    return chrome_run_yl


def sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, text):
    for char in text:
        shared_chrome_message_text.value = ord(char)
        while shared_chrome_message_text.value != -1:
            pass

    shared_chrome_message_text_print.value = True


def chrome_cleak(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                 shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                 shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                 shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                 shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                 shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                 shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                 shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                 shared_chrome_message_text_print, shared_chrome_message_text,
                 shared_chrome_driver_run_zt, chrome
                 ):
    global chrome_driver_ing

    if not shared_chrome_driver_run_zt.value:
        if shared_chrome_s_run_ing.value:
            Chrome_s_stop(shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                          shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                          shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                          shared_chrome_s_run_ing)
            while shared_chrome_s_run_ing.value:
                pass
        if shared_chrome_process_s_run_ing.value:
            Process_stop(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                         shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                         shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                         shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                         shared_chrome_process_s_run_ing)
            while shared_chrome_process_s_run_ing.value:
                pass

        chrome.quit()
        chrome_driver_ing = False
        sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '无')
        return True


def chrome_open(chrome_config_yl, shared_chrome_message_text_print, shared_chrome_message_text):
    global chrome_driver_ing
    # 打开浏览器并跳转到指定页面
    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '浏览器已启动')
    chrome = webdriver.Chrome(service=chrome_config_yl[1], options=chrome_config_yl[0])
    chrome_driver_ing = True
    return chrome


# 用户数据检测
def user_data_jc(shared_chrome_message_text_print, shared_chrome_message_text):
    if os.path.exists(file_dir_id.user_data_ip + '\\' + file_dir_id.user_data_name):
        sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '已检测到用户信息，正在尝试登陆中')
        return True

    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '未检测到用户信息，请用户操作登录')
    return False


# 用户数据自动登录
def user_data_zddl(chrome, url, shared_chrome_message_text_print, shared_chrome_message_text):
    global user_data_up

    with open(file_dir_id.user_data_ip + '\\' + file_dir_id.user_data_name, 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        chrome.add_cookie(cookie)
    chrome.get(url=url)

    time.sleep(2)
    if chrome.title != '运输安全管理平台':
        sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text,
                      '尝试登录失败，用户信息已过期，请用户操作登录，以刷新用户数据')
        user_data_up = False
        return False

    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text,
                  '已跳转至\"' + str(chrome.title) + '\"')
    return True


# 用户手动登录
def user_sddl(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
              shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
              shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
              shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
              shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
              shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
              shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
              shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
              shared_chrome_message_text, shared_chrome_message_text_print,
              shared_chrome_driver_run_zt, chrome,
              ):
    time.sleep(3)
    while chrome.title == '京东-欢迎登录':
        if chrome_cleak(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                        shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                        shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                        shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                        shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                        shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                        shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                        shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                        shared_chrome_message_text_print, shared_chrome_message_text,
                        shared_chrome_driver_run_zt, chrome):
            return False

    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '用户已登录，正在跳转中')

    while chrome.title != '运输安全管理平台':
        if chrome_cleak(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                        shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                        shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                        shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                        shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                        shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                        shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                        shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                        shared_chrome_message_text_print, shared_chrome_message_text,
                        shared_chrome_driver_run_zt, chrome):
            return False

    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text,
                  '已跳转至\"' + str(chrome.title) + '\"')
    time.sleep(1)
    with open(file_dir_id.user_data_ip + '\\' + file_dir_id.user_data_name, 'w') as f:
        f.write(json.dumps(chrome.get_cookies()))

    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text,
                  '用户数据已更新' if user_data_up else '用户数据已保存')
    return True


# 网页跳转
def get_url(
        shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
        shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
        shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
        shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
        shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
        shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
        shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
        shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
        shared_chrome_message_text_print, shared_chrome_message_text,
        shared_chrome_driver_run_zt, chrome, url,
):
    sys_print_use(shared_chrome_message_text_print, shared_chrome_message_text, '已跳转至指定网站，正在检测用户信息')
    chrome.get(url)

    if user_data_jc(shared_chrome_message_text_print, shared_chrome_message_text):
        if user_data_zddl(chrome, url, shared_chrome_message_text_print, shared_chrome_message_text):
            return True

    return user_sddl(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                     shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                     shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                     shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                     shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                     shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                     shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                     shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                     shared_chrome_message_text, shared_chrome_message_text_print,
                     shared_chrome_driver_run_zt, chrome)


# 注册单个子进程
def Process_add(target, process_s_bq_add, process_s_id):
    global chrome_processes_s_id
    process_s_bq_add.value = target

    while process_s_id.value == -1:
        pass

    chrome_processes_s_id.append(process_s_id.value)
    process_s_id.value = -1


# 配置各模块进程
def Process_config(s_bq_add, s_id):
    Process_add(1, s_bq_add, s_id)
    Process_add(2, s_bq_add, s_id)
    Process_add(3, s_bq_add, s_id)


# 启动单个子进程
def process_start(target, s_bq_start, jcmk_run_zt, jcmk_run_ing):
    jcmk_run_zt.value = True
    s_bq_start.value = target

    while not jcmk_run_ing.value:
        pass


# 启动所有子进程
def Process_start(shared_chrome_process_s_error_jc_run_zt, shared_chrome_error_jc_process_s_run_ing,
                  shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                  shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                  shared_chrome_driver_process_bq_start, shared_chrome_process_s_run_ing):
    process_start(chrome_processes_s_id[0], shared_chrome_driver_process_bq_start,
                  shared_chrome_process_s_error_jc_run_zt, shared_chrome_error_jc_process_s_run_ing)
    process_start(chrome_processes_s_id[1], shared_chrome_driver_process_bq_start,
                  shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing)
    process_start(chrome_processes_s_id[2], shared_chrome_driver_process_bq_start,
                  shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing)

    shared_chrome_process_s_run_ing.value = True


# 停止单个子进程
def process_stop(target, stop_bz, stop, zt, ing):
    zt.value = False
    while ing.value:
        pass
    stop.value = target

    while not stop_bz.value:
        pass

    stop_bz.value = False

    chrome_processes_s_id.pop(chrome_processes_s_id.index(target))


# 停止所有子进程
def Process_stop(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                 shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                 shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                 shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                 shared_chrome_process_s_run_ing):
    process_stop(chrome_processes_s_id[2], shared_chrome_driver_process_stop_bz, shared_chrome_driver_process_bq_stop,
                 shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing)
    process_stop(chrome_processes_s_id[1], shared_chrome_driver_process_stop_bz, shared_chrome_driver_process_bq_stop,
                 shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing)
    process_stop(chrome_processes_s_id[0], shared_chrome_driver_process_stop_bz, shared_chrome_driver_process_bq_stop,
                 shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing)
    shared_chrome_process_s_run_ing.value = False


def chrome_s_start(zt, ing):
    zt.value = True
    while not ing.value:
        pass


def Chrome_s_start(error_jc_run_zt, error_jc_run_ing, jcmk_run_zt, jcmk_run_ing, Voice_user_run_zt, Voice_user_run_ing,
                   s_run_ing):
    chrome_s_start(error_jc_run_zt, error_jc_run_ing)
    chrome_s_start(jcmk_run_zt, jcmk_run_ing)
    chrome_s_start(Voice_user_run_zt, Voice_user_run_ing)

    s_run_ing.value = True


def chrome_s_stop(zt, ing):
    zt.value = False

    while ing.value:
        pass


def Chrome_s_stop(error_jc_run_zt, error_jc_run_ing,
                  jcmk_run_zt, jcmk_run_ing,
                  Voice_user_run_zt, Voice_user_run_ing,
                  s_run_ing):
    chrome_s_stop(Voice_user_run_zt, Voice_user_run_ing)
    chrome_s_stop(jcmk_run_zt, jcmk_run_ing)
    chrome_s_stop(error_jc_run_zt, error_jc_run_ing)
    s_run_ing.value = False


def chrome_driver(shared_chrome_driver_process_run_zt, shared_chrome_driver_process_run_ing,
                  shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                  shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                  shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                  shared_chrome_driver_run_zt, shared_chrome_driver_run_ing,
                  shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                  shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                  shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                  shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                  shared_chrome_jccz_title_queue, shared_chrome_jccz_current_url_queue,
                  shared_chrome_jccz_page_source_queue, shared_chrome_error_page_source_queue,
                  shared_chrome_message_text, shared_chrome_message_text_print,
                  shared_chrome_driver_process_bq_add, shared_chrome_driver_process_id,
                  shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                  shared_chrome_driver_process_bq_start, shared_chrome_find_button_zt):
    global _chrome_driver
    chrome_run_config = chrome_config()  # 配置浏览器并生成启动依赖
    while shared_chrome_driver_process_run_zt.value:
        if not shared_chrome_driver_process_run_ing.value:
            shared_chrome_driver_process_run_ing.value = True

        if (not shared_chrome_driver_run_zt.value) and shared_chrome_driver_run_ing.value:
            shared_chrome_driver_run_ing.value = False

        while shared_chrome_driver_run_zt.value:
            if not shared_chrome_driver_run_ing.value:
                shared_chrome_driver_run_ing.value = True

            if not chrome_driver_ing:
                _chrome_driver = chrome_open(chrome_run_config, shared_chrome_message_text_print,
                                             shared_chrome_message_text)  # 打开浏览器

                if not get_url(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                               shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                               shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                               shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                               shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                               shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                               shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                               shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                               shared_chrome_message_text_print, shared_chrome_message_text,
                               shared_chrome_driver_run_zt, _chrome_driver, login_url):  # 跳转至指定网站
                    shared_chrome_driver_run_ing.value = False
                    break
                Process_config(shared_chrome_driver_process_bq_add, shared_chrome_driver_process_id)

                Process_start(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                              shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                              shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                              shared_chrome_driver_process_bq_start, shared_chrome_process_s_run_ing)

            error_find_button = _chrome_driver.find_element(By.CLASS_NAME, 'el-button.el-button--primary')
            while chrome_driver_ing:
                shared_chrome_jccz_title_queue.put(str(_chrome_driver.title))
                shared_chrome_jccz_current_url_queue.put(str(_chrome_driver.current_url))
                shared_chrome_jccz_page_source_queue.put(str(_chrome_driver.page_source))
                shared_chrome_error_page_source_queue.put(str(_chrome_driver.page_source))

                try:
                    if shared_chrome_find_button_zt.value:
                        shared_chrome_find_button_zt.value = False
                        error_find_button.click()
                except:
                    pass

                if not shared_chrome_s_run_ing.value:
                    Chrome_s_start(shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                                   shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                                   shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                                   shared_chrome_s_run_ing)

                if not shared_chrome_driver_run_zt.value:
                    shared_chrome_jccz_title_queue.put(str("!"))
                    shared_chrome_jccz_current_url_queue.put(str("!"))
                    shared_chrome_jccz_page_source_queue.put(str("!"))
                    shared_chrome_error_page_source_queue.put(str("!"))
                    chrome_cleak(shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
                                 shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
                                 shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
                                 shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
                                 shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
                                 shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
                                 shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
                                 shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                                 shared_chrome_message_text_print, shared_chrome_message_text,
                                 shared_chrome_driver_run_zt, _chrome_driver)

    if (not shared_chrome_driver_process_run_zt.value) and shared_chrome_driver_process_run_ing.value:
        shared_chrome_driver_process_run_ing.value = False
        return


# 浏览器启动检测

def chrome_start_jc(shared_chrome_driver_process_run_zt, shared_chrome_driver_process_run_ing,
                    shared_chrome_driver_run_zt, shared_chrome_driver_run_ing,
                    shared_chrome_driver_process_bq_add, shared_chrome_driver_process_id,
                    shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
                    shared_chrome_start, shared_chrome_driver_process_bq_start, shared_chrome_start_jc_zt):
    while shared_chrome_start_jc_zt.value:
        if shared_chrome_start.value:
            shared_chrome_driver_process_run_zt.value = True
            shared_chrome_driver_process_bq_add.value = 0

            while shared_chrome_driver_process_id.value == -1:
                pass
            chrome_driver_processes_id = shared_chrome_driver_process_id.value
            shared_chrome_driver_process_id.value = -1

            shared_chrome_driver_process_bq_start.value = chrome_driver_processes_id

            while not shared_chrome_driver_process_run_ing.value:
                pass

            shared_chrome_driver_run_zt.value = True

            while not shared_chrome_driver_run_ing.value:
                pass

            while shared_chrome_start.value:
                pass

            shared_chrome_driver_run_zt.value = False

            while shared_chrome_driver_run_ing.value:
                pass

            shared_chrome_driver_process_run_zt.value = False

            while shared_chrome_driver_process_run_ing.value:
                pass

            shared_chrome_driver_process_bq_stop.value = chrome_driver_processes_id

            while not shared_chrome_driver_process_stop_bz.value:
                pass
            shared_chrome_driver_process_stop_bz.value = False
