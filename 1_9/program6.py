# 工资部门将每个支付周期的雇员信息的列表保存到一个文本文件中。该文件每一行格式如下：
# <last name><hourly wage><hours worked>
# 编写一个程序，让用户输入文件名并且向终端输出报表，展示在给定周期应该向每一位雇员支付工资。
# 这个报表应该是表格的格式，并且具有相应的表头。每一行应该包含雇员的名称、工作的小时数，以及该周期所支付的工资。


class ReportTable:
    def __init__(self, filepath):
        self.inf = []
        with open(filename) as f:
            information = f.readlines()
            for i in information:
                string = i.split(',')

                d = {'last name': string[0], 'hourly wage': string[1], 'hours worked': string[2].replace('\n','')}
                self.inf.append(d)
            f.close()

    def print_report(self):
        with open('report.csv', 'w') as f:
            f.write('last name,hours worked,wage\n')
            for inf in self.inf:
                wage = float(inf['hours worked']) * float(inf['hourly wage'])
                print('{},{},{}'.format(inf['last name'], inf['hours worked'], wage))
                f.write(inf['last name']+','+inf['hours worked']+',{}\n'.format(wage))

            f.close()


if __name__ == '__main__':
    filename = input('请输入文件名：')
    ReportTable(filename).print_report()
