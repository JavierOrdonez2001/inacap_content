const holidays = ['01/06', '04/01', '12/25']

const date = new Date(`2022-${holidays[2]}`)

const diaSemana = date.getDate()
console.log(diaSemana)