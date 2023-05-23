import os
import datetime

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

current_date = start_date
while current_date <= end_date:
    # 构造目录路径
    directory_path = os.path.join(
        ".", str(current_date.year), f"{current_date.month:02d}", f"{current_date.day:02d}"
    )
    
    # 创建目录
    os.makedirs(directory_path, exist_ok=True)
    # 在目录中创建 .gitkeep 文件
    gitkeep_file = os.path.join(directory_path, '.gitkeep')
    with open(gitkeep_file, 'w') as file:
        pass

    # 增加一天
    current_date += datetime.timedelta(days=1)
