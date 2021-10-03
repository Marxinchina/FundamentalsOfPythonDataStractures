# 一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，再加上加班费。
# 加班费等于总的加班时间乘以每小时薪水的1.5倍。编写一个程序，以每小时的薪水、总的常规工作时间和总的加班时间作为参数，
# 并且显示一个雇员的总周薪

class Wage:
    def __init__(self, wage, work_time, overtime):
        self.week_wage = wage * work_time + 1.5 * wage * overtime

    def __str__(self):
        return '你本周的周薪为{}元'.format(self.week_wage)


if __name__ == '__main__':
    wage = float(input('你每小时挣多少钱（元）：'))
    work_time = float(input('本周你不算加班上班多长时间（小时）：'))
    overtime = float(input('本周你加班多少时间（小时）：'))
    print(Wage(wage, work_time, overtime))
