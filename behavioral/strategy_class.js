// 定义一系列计算年终奖的算法
const bounsStrategy = {
    'S': (salary) => salary * 4,
    'A': (salary) => salary * 3,
    'B': (salary) => salary * 2,
    // 添加 S+ 和 C 算法
    'SP': (salary) => salary * 5,
    'C': (salary) => salary,
}

class Bouns {
    constructor(name, salary) {
        this.name = name;
        this.salary = salary
        // 计算方法通过属性来设定，这样可以容易被替换
        this.calculate = null;
    }

    get bouns() {
        return this.calculate(this.salary)
    }

    print() {
        console.log(this.name, 'get', this.bouns)
    }
}

jackBouns = new Bouns('jack', 10000)
jackBouns.calculate = bounsStrategy.S
jackBouns.print()

lindaBouns = new Bouns('linda', 10000)
lindaBouns.calculate = bounsStrategy.A
lindaBouns.print()

seanBouns = new Bouns('sean', 10000)
seanBouns.calculate = bounsStrategy.B
seanBouns.print()

// 现在需求变化了，添加 S+ 作为最高级，C 级 作为最低级
// jack 从 S 调整到 S+
// sean 从 B 调整到 C
console.log('需求改变以后......')

jackBouns.calculate = bounsStrategy.SP
jackBouns.print()

lindaBouns.print()

seanBouns.calculate = bounsStrategy.C
seanBouns.print()

// 从上面的计算年终的算法可以看出
// 需求改变以后只需要替代原来算法就可实现了