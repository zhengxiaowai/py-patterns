// 定义一系列计算年终奖的算法
const bounsStrategy = {
    'S': (salary) => salary * 4,
    'A': (salary) => salary * 3,
    'B': (salary) => salary * 2,
    // 添加 S+ 和 C 算法
    'SP': (salary) => salary * 5,
    'C': (salary) => salary,
}

function calculateBouns(name, strategy, salary) {
    return `${name} get ${strategy(salary)}`

}

console.log(calculateBouns('jack', bounsStrategy.S, 10000))
console.log(calculateBouns('linda', bounsStrategy.A, 10000))
console.log(calculateBouns('sean', bounsStrategy.B, 10000))

// 现在需求变化了，添加 S+ 作为最高级，C 级 作为最低级
// jack 从 S 调整到 S+
// sean 从 B 调整到 C
console.log('需求改变以后......')

console.log(calculateBouns('jack', bounsStrategy.SP, 10000))
console.log(calculateBouns('linda', bounsStrategy.A, 10000))
console.log(calculateBouns('sean', bounsStrategy.C, 10000))