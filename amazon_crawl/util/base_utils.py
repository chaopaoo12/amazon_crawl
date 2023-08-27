from functools import wraps

def retry(*args, **kwargs):
    def warpp(func):
        @wraps(func)
        def inner():
            ret = func()
            max_retry = kwargs.get('max_retry')
            # 不传默认重试3次
            if not max_retry:
                max_retry = 3
            number = 0
            if not ret:
                while number < max_retry:
                    number += 1
                    print("尝试第:{}次".format(number))
                    result = func()
                    if result:
                        break
        return inner
    return warpp