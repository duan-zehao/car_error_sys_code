import pyttsx3

engine = pyttsx3.init()


# 扬声器配置
def speech_config():
    global engine

    engine.setProperty('volume', 1.0)


# 扬声器控制总模块
def Voice_user(shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
               shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
               shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text):
    Voice_text = ''
    speech_config()
    while shared_chrome_process_s_Voice_user_run_zt.value:
        if not shared_chrome_process_s_Voice_user_run_ing.value:
            shared_chrome_process_s_Voice_user_run_ing.value = True

        if (not shared_chrome_Voice_user_run_zt.value) and shared_chrome_Voice_user_run_ing.value:
            shared_chrome_Voice_user_run_ing.value = False

        while shared_chrome_Voice_user_run_zt.value:
            if not shared_chrome_Voice_user_run_ing.value:
                shared_chrome_Voice_user_run_ing.value = True

            if (shared_chrome_Voice_text.value != -1) and (not shared_chrome_Voice_text_grade.value):
                Voice_text = Voice_text + chr(shared_chrome_Voice_text.value)
                shared_chrome_Voice_text.value = -1

            if (shared_chrome_Voice_text.value != -1) and shared_chrome_Voice_text_grade.value:
                Voice_text = Voice_text + chr(shared_chrome_Voice_text.value)
                shared_chrome_Voice_text.value = -1

            # 判断发声命令是否成立
            if shared_chrome_Voice_text_send_user.value:
                shared_chrome_Voice_text_send_user.value = False
                engine.say(Voice_text)
                engine.runAndWait()
                Voice_text = ''
                if shared_chrome_Voice_text_grade.value:
                    shared_chrome_Voice_text_grade.value = False

    if (not shared_chrome_process_s_Voice_user_run_zt.value) and shared_chrome_process_s_Voice_user_run_ing.value:
        shared_chrome_process_s_Voice_user_run_ing.value = False
