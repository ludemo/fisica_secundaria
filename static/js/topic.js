var exercise = document.querySelectorAll('button')
console.log(exercise)
var count = 0
exercise.forEach(listElement => {
  listElement.addEventListener('click', ()=>{
      listElement.classList.toggle('arrow')
      let solution = listElement.nextElementSibling
      console.log(solution.classList);
      if (solution.classList == 'exercise__solution exercise__solution--display') {
        console.log('aqui');
        solution.classList.remove('exercise__solution--display')
      } else {
        solution.classList.add('exercise__solution--display')
      }
        
      console.log(listElement);
      exercise.forEach( ex => {
        if (listElement !== ex) {
          ex.nextElementSibling.classList.remove('exercise__solution--display')
        }
      })
  })
})