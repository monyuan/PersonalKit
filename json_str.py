"""
    输入的数据返回json格式字符串
"""
import json


def MessageConstructor(status, message, data=""):
    w_data = {
        "status": status,
        "message": message,
        "data": data
    }

    # 分段保存字符串
    if not w_data['data']:
        result = "{" + '"status":"{0}","message":"{1}"'.format(w_data['status'], w_data['message']) + "}"
        return result

    else:
        json_str = json.dumps(data)
        data_str = '"status":"{0}","message":"{1}",'.format(w_data['status'], w_data['message'])
        result = "{" + data_str + '"data":' + json_str + "}"
        return result

#
# def test(data):
#     with open('data.json', 'w') as f:
#         json.dump(data, f)


if __name__ == '__main__':
    info = {"stu101": "Tim", "stu102": "Hu"}
    x = MessageConstructor("0", "success", info)
    # 写入文件查看输出是否正确
    # test(x)
