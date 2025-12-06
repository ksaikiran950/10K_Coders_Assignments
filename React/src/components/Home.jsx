import { useEffect } from 'react'
import AddTodo from './AddTodo'

const Home = () => {
    const[todos,setTodos]=useState([])
    let login_user=localStorage.getItem(user_details)
    useEffect(()=>{
        const getAllTodos = async()=>{
            try {
                let response = await fetch("http://localhost:3001/todos");
                let jsonResponse= await response.json()
                setTodos(jsonResponse)
            } catch (error) {
                console.log(error)
            }
        }
        getAllTodos()
    },[todos])
  return (
    <div>
      <AddTodo/>
      {
       todos.length==0?(<h1>No todos found</h1>):(
        todos.AddTodo
       )
      }

    </div>
  ))
}

export default Home
