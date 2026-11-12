# пока программа работает, данные живут в памяти ПК
# ПЕРСИСТЕНТНОСТЬ - возможность сохранять данные после выключения программы

with open('text.txt', 'w', encoding='UTF-8') as f:
    f.write('hello autotest world!')
    f.write('Second Line!')

    # 'w' - create and write / if exists - overwrite
    # 'r' - read
    # 'a' - create and append
    # 'r +' - read and write
    # 'rb' / 'wb' - PDF screenshots


# ---- Earlier------:
# file = open("data.txt", "w")
# file.write("Hello World")
# file.close()

def log_test_res(test_name,status):
    with open("test_run.log","a",encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_res('test login', 'passed')
log_test_res('test logout', 'failed')
log_test_res('registration', 'failed')