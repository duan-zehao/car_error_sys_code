import multiprocessing

shared_chrome_start = multiprocessing.Value('b', False)
shared_main_sys_zt = multiprocessing.Value('b', False)
shared_chrome_start_jc_zt = multiprocessing.Value('b', False)
shared_sys_reset = multiprocessing.Value('b', False)

shared_chrome_driver_process_bq_add = multiprocessing.Value('i', -1)
shared_chrome_driver_process_bq_start = multiprocessing.Value('i', -1)
shared_chrome_driver_process_bq_stop = multiprocessing.Value('i', -1)
shared_chrome_driver_process_stop_bz = multiprocessing.Value('b', False)
shared_chrome_driver_process_id = multiprocessing.Value('i', -1)
shared_chrome_driver_process_run_zt = multiprocessing.Value('b', False)
shared_chrome_driver_process_run_ing = multiprocessing.Value('b', False)
shared_chrome_driver_run_zt = multiprocessing.Value('b', False)
shared_chrome_driver_run_ing = multiprocessing.Value('b', False)

shared_chrome_run_zt = multiprocessing.Value('b', False)
shared_chrome_run_ing = multiprocessing.Value('b', False)
shared_chrome_message_text = multiprocessing.Value('i', -1)
shared_chrome_message_text_print = multiprocessing.Value('b', False)
shared_chrome_yxjc = multiprocessing.Value('b', False)
shared_chrome_jccz_title_queue = multiprocessing.Queue()
shared_chrome_jccz_current_url_queue = multiprocessing.Queue()
shared_chrome_jccz_page_source_queue = multiprocessing.Queue()
shared_chrome_error_page_source_queue = multiprocessing.Queue()
shared_chrome_queue_ing = multiprocessing.Value('b', False)
shared_chrome_button_zt = multiprocessing.Value('b', False)

shared_chrome_process_s_run_ing = multiprocessing.Value('b', False)
shared_chrome_process_s_run_zt = multiprocessing.Value('b', False)
shared_chrome_s_run_ing = multiprocessing.Value('b', False)
shared_chrome_s_run_zt = multiprocessing.Value('b', False)

shared_chrome_process_s_error_jc_run_zt = multiprocessing.Value('b', False)
shared_chrome_process_s_error_jc_run_ing = multiprocessing.Value('b', False)
shared_chrome_error_jc_run_zt = multiprocessing.Value('b', False)
shared_chrome_error_jc_run_ing = multiprocessing.Value('b', False)
shared_chrome_error_jc_word_zt = multiprocessing.Value('b', False)
shared_chrome_find_button_zt = multiprocessing.Value('b', False)

shared_chrome_process_s_jcmk_run_ing = multiprocessing.Value('b', False)
shared_chrome_process_s_jcmk_run_zt = multiprocessing.Value('b', False)
shared_chrome_jcmk_run_zt = multiprocessing.Value('b', False)
shared_chrome_jcmk_run_ing = multiprocessing.Value('b', False)
shared_chrome_jcmk_word_ing = multiprocessing.Value('b', False)
shared_chrome_jcmk_word_value = multiprocessing.Value('b', False)

shared_chrome_process_s_Voice_user_run_ing = multiprocessing.Value('b', False)
shared_chrome_process_s_Voice_user_run_zt = multiprocessing.Value('b', False)
shared_chrome_Voice_user_run_zt = multiprocessing.Value('b', False)
shared_chrome_Voice_user_run_ing = multiprocessing.Value('b', False)
shared_chrome_Voice_text_sys_stop = multiprocessing.Value('b', True)
shared_chrome_Voice_text_user_stop = multiprocessing.Value('b', False)
shared_chrome_Voice_text_send_user = multiprocessing.Value('b', False)
shared_chrome_Voice_text = multiprocessing.Value('i', -1)
shared_chrome_Voice_text_grade = multiprocessing.Value('b', False)

main_process_ml = []

chrome_driver_jk = (
    shared_chrome_driver_process_run_zt, shared_chrome_driver_process_run_ing,
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
    shared_chrome_driver_process_bq_start, shared_chrome_find_button_zt,
)
chrome_error_jc_start_jk = (
    shared_chrome_process_s_error_jc_run_zt, shared_chrome_process_s_error_jc_run_ing,
    shared_chrome_error_jc_run_zt, shared_chrome_error_jc_run_ing,
    shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
    shared_chrome_error_jc_word_zt, shared_chrome_error_page_source_queue, shared_chrome_find_button_zt,
    shared_chrome_Voice_user_run_ing
)
jcmk_start_jk = (
    shared_chrome_process_s_jcmk_run_zt, shared_chrome_process_s_jcmk_run_ing,
    shared_chrome_jcmk_run_zt, shared_chrome_jcmk_run_ing,
    shared_chrome_jccz_page_source_queue, shared_chrome_jccz_current_url_queue, shared_chrome_jccz_title_queue,
    shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
    shared_chrome_error_jc_word_zt, shared_chrome_Voice_user_run_ing
)
Voice_user_jk = (
    shared_chrome_process_s_Voice_user_run_zt, shared_chrome_process_s_Voice_user_run_ing,
    shared_chrome_Voice_user_run_zt, shared_chrome_Voice_user_run_ing,
    shared_chrome_Voice_text_send_user, shared_chrome_Voice_text_grade, shared_chrome_Voice_text,
)

sys_print_jk = (
    shared_chrome_driver_process_run_ing, shared_chrome_driver_run_ing,
    shared_chrome_process_s_error_jc_run_ing, shared_chrome_error_jc_run_ing,
    shared_chrome_process_s_jcmk_run_ing, shared_chrome_jcmk_run_ing,
    shared_chrome_process_s_Voice_user_run_ing, shared_chrome_Voice_user_run_ing,
    shared_chrome_process_s_run_ing, shared_chrome_s_run_ing,
    shared_chrome_message_text_print, shared_chrome_message_text,
    shared_chrome_start, shared_main_sys_zt, shared_sys_reset
)
chrome_start_jc_jk = (
    shared_chrome_driver_process_run_zt, shared_chrome_driver_process_run_ing,
    shared_chrome_driver_run_zt, shared_chrome_driver_run_ing,
    shared_chrome_driver_process_bq_add, shared_chrome_driver_process_id,
    shared_chrome_driver_process_bq_stop, shared_chrome_driver_process_stop_bz,
    shared_chrome_start, shared_chrome_driver_process_bq_start, shared_chrome_start_jc_zt,
)
