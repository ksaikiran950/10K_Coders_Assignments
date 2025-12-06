import { useState } from "react";

const AddTodo = ({ userId }) => {   // ✔ userId received from Login

  const [todo, setTodo] = useState("");

  const addBtn = () => {
    const addTodo = async () => {
      try {

        let res = await fetch("http://localhost:3001/todos", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            text: todo,
            user_id: userId     
          })
        });

        let json = await res.json();
        console.log("Todo added:", json);

      } catch (error) {
        console.log(error);
      }
    };

    addTodo(); // keep structure same
  };

  return (
    <div>
      <input 
        type="text"
        placeholder="add your todos"
        value={todo}
        onChange={(e) => setTodo(e.target.value)}
      />

      <button onClick={addBtn}>Add</button>
    </div>
  );
};

export default AddTodo;
