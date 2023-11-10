import uno
import officehelper
from com.sun.star.beans import PropertyValue
import time
from gen import generate_passwords

CTX = uno.getComponentContext()

def create_instance(name, with_context=False):
    xContext = officehelper.bootstrap()
    print("Connected to a running office ...")
    SM = xContext.getServiceManager()
    available = "not available" if SM is None else "available"
    print("remote ServiceManager is " + available)

    if with_context:
        instance = SM.createInstanceWithContext(name, CTX)
    else:
        instance = SM.createInstance(name)
    return instance

def attempt_open_document(desktop, path, password):
    args = (
        PropertyValue(Name='Password', Value=password),
        PropertyValue(Name='Hidden', Value=True),
    )
    doc = desktop.loadComponentFromURL(path, '_default', 0, args)
    return doc

def close_document(doc):
    try:
        if hasattr(doc, "close"):
            doc.close(True)
        else:
            doc.dispose()
    except Exception as e:
        print("Error closing the document:", e)


if __name__ == "__main__":
    desktop = create_instance('com.sun.star.frame.Desktop', True)
    path = uno.systemPathToFileUrl('/home/hyyou/dev/libreoffice/py/pwd_test.odt')
    max_attempts = 10000

    start_time = time.time()
    attempts = 0  # 初始化尝试次数

    for pwd in generate_passwords():  # 正确迭代生成的密码
        attempts += 1  # 增加尝试次数
        print(f"{attempts}:{pwd}")
        doc = attempt_open_document(desktop, path, pwd)
        if doc is not None:
            close_document(doc)
            print('Success with password:', pwd)
            break
        if attempts >= max_attempts:  # 如果达到最大尝试次数，则停止
            print('Reached maximum number of attempts')
            break

    end_time = time.time()

    total_duration = end_time - start_time
    print(f"Total time for {attempts} attempts: {total_duration} seconds.")
    if attempts:
        print(f"Average time per attempt: {total_duration/attempts} seconds.")
